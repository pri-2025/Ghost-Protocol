package com.citi.drunix.ghostprotocol.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.time.Instant;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;

@RestController
@RequestMapping("/api/v1/banking")
@CrossOrigin(origins = "*")
public class TransactionController {

    private final RestTemplate restTemplate;

    @Value("${sentinel.url:http://localhost:8000/api/v1/sentinel/evaluate}")
    private String sentinelUrl;

    // Drunix DLT State Simulation Store
    private final AtomicLong blockHeight = new AtomicLong(1048200L);
    private final List<Map<String, Object>> drunixLedgerBlocks = Collections.synchronizedList(new ArrayList<>());
    private final List<Map<String, Object>> honeypotIsolatedTxs = Collections.synchronizedList(new ArrayList<>());

    public TransactionController(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    @GetMapping("/health")
    public ResponseEntity<Map<String, Object>> healthCheck() {
        Map<String, Object> status = new HashMap<>();
        status.put("status", "UP");
        status.put("service", "Citi Core Banking DLT Gateway");
        status.put("drunix_current_block", blockHeight.get());
        status.put("sentinel_endpoint", sentinelUrl);
        return ResponseEntity.ok(status);
    }

    @PostMapping("/transfer")
    public ResponseEntity<Map<String, Object>> processTransaction(@RequestBody Map<String, Object> requestPayload) {
        Map<String, Object> responseMap = new HashMap<>();
        String txId = requestPayload.containsKey("transaction_id") && requestPayload.get("transaction_id") != null
                ? requestPayload.get("transaction_id").toString()
                : "TX-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase();

        // Extract structural payload markers with robust fallbacks
        double amount = Double.parseDouble(requestPayload.getOrDefault("amount", "125000.0").toString());
        int velocity = Integer.parseInt(requestPayload.getOrDefault("velocity_1h", "14").toString());
        double deviceRisk = Double.parseDouble(requestPayload.getOrDefault("device_risk_score", "0.42").toString());
        double entropy = Double.parseDouble(requestPayload.getOrDefault("iso_msg_entropy", "3.85").toString());
        double latency = Double.parseDouble(requestPayload.getOrDefault("settlement_latency_ms", "18.5").toString());
        boolean simAttack = Boolean.parseBoolean(requestPayload.getOrDefault("is_adversarial_simulated", "false").toString());

        // 1. Build the payload for the Mirror-Verse Sentinel Validation Mesh
        Map<String, Object> sentinelPayload = new HashMap<>();
        sentinelPayload.put("transaction_id", txId);
        sentinelPayload.put("amount", amount);
        sentinelPayload.put("velocity_1h", velocity);
        sentinelPayload.put("device_risk_score", deviceRisk);
        sentinelPayload.put("iso_msg_entropy", entropy);
        sentinelPayload.put("settlement_latency_ms", latency);
        sentinelPayload.put("is_adversarial_simulated", simAttack);

        try {
            // 2. Perform parallel telemetry evaluation against Mirror-Verse Sentinel
            ResponseEntity<Map> sentinelResponse = restTemplate.postForEntity(sentinelUrl, sentinelPayload, Map.class);
            Map<String, Object> evaluationResult = sentinelResponse.getBody();

            if (evaluationResult != null && "SANDBOX_ISOLATE".equals(evaluationResult.get("status"))) {
                // Ghost Protocol triggered: Route to isolated simulation infrastructure
                Map<String, Object> honeypotRecord = new HashMap<>();
                honeypotRecord.put("transaction_id", txId);
                honeypotRecord.put("isolated_at", Instant.now().toString());
                honeypotRecord.put("reconstruction_error", evaluationResult.get("reconstruction_error"));
                honeypotRecord.put("telemetry", evaluationResult);
                honeypotIsolatedTxs.add(honeypotRecord);

                responseMap.put("transaction_id", txId);
                responseMap.put("execution_status", "ROUTED_TO_HONEYPOT");
                responseMap.put("drunix_block_state", "MUTATION_BLOCKED");
                responseMap.put("message", "Adversarial neural perturbation detected. Transaction safely shunted to tracking sandbox.");
                responseMap.put("telemetry", evaluationResult);
                return ResponseEntity.status(202).body(responseMap);
            }

            // 3. Normal Path: Transaction committed to Drunix Distributed Ledger State Roots
            long newBlock = blockHeight.incrementAndGet();
            String blockHash = "0x" + UUID.randomUUID().toString().replace("-", "") + "citi";
            
            Map<String, Object> blockData = new HashMap<>();
            blockData.put("block_height", newBlock);
            blockData.put("block_hash", blockHash);
            blockData.put("transaction_id", txId);
            blockData.put("amount", amount);
            blockData.put("status", "COMMITTED");
            blockData.put("timestamp", Instant.now().toString());
            drunixLedgerBlocks.add(blockData);

            responseMap.put("transaction_id", txId);
            responseMap.put("execution_status", "SUCCESSFULLY_SETTLED");
            responseMap.put("drunix_block_state", "COMMITTED_BLOCK_" + newBlock);
            responseMap.put("block_hash", blockHash);
            responseMap.put("message", "Transaction verified safe against adversarial shifts.");
            responseMap.put("telemetry", evaluationResult);
            return ResponseEntity.ok(responseMap);

        } catch (Exception e) {
            // If Sentinel is temporarily unreachable, return graceful diagnostic error
            responseMap.put("error", "Failed to communicate with Sentinel routing mesh.");
            responseMap.put("details", e.getMessage());
            responseMap.put("transaction_id", txId);
            responseMap.put("fallback_warning", "Production execution halted in fail-safe mode.");
            return ResponseEntity.status(503).body(responseMap);
        }
    }

    @GetMapping("/ledger/blocks")
    public ResponseEntity<Map<String, Object>> getLedgerBlocks() {
        Map<String, Object> result = new HashMap<>();
        result.put("current_height", blockHeight.get());
        result.put("committed_blocks", drunixLedgerBlocks);
        result.put("honeypot_isolated_count", honeypotIsolatedTxs.size());
        return ResponseEntity.ok(result);
    }

    @GetMapping("/honeypot/records")
    public ResponseEntity<List<Map<String, Object>>> getHoneypotRecords() {
        return ResponseEntity.ok(honeypotIsolatedTxs);
    }
}

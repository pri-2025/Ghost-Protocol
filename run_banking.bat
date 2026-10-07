@echo off
echo ===================================================
echo   CITI DRUNIX: PROJECT GHOST PROTOCOL
echo   Starting Core Banking Gateway (Spring Boot :8080)
echo ===================================================
cd core-banking
..\tools\apache-maven-3.9.6\bin\mvn.cmd spring-boot:run
pause

#!/bin/bash

# Spring PetClinic Automation Test Runner

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🐾 Spring PetClinic Automation Tests${NC}"
echo ""

# Check if application is running
if ! curl -s http://localhost:8080 > /dev/null 2>&1; then
    echo -e "${YELLOW}⚠️  Warning: Application not running on localhost:8080${NC}"
    echo "Please start the application first:"
    echo "  cd /Users/jhon/projects/spring-petclinic"
    echo "  ./mvnw spring-boot:run"
    echo ""
    echo "Or use Docker:"
    echo "  docker-compose up -d"
    echo ""
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Change to tests directory
cd "$(dirname "$0")/.."

# Install dependencies if needed
if [ ! -d "venv" ] && [ ! -f "requirements.txt" ]; then
    echo -e "${YELLOW}Installing dependencies...${NC}"
    pip3 install -r requirements.txt
    python3 -m playwright install chromium
fi

# Run tests
echo -e "${GREEN}Running tests...${NC}"
echo ""

# Default: run all tests
if [ $# -eq 0 ]; then
    pytest -v --html=reports/report.html --json-report --json-report-file=reports/report.json
else
    pytest "$@"
fi

echo ""
echo -e "${GREEN}✅ Tests completed!${NC}"
echo "Reports:"
echo "  - HTML: $(pwd)/reports/report.html"
echo "  - JSON: $(pwd)/reports/report.json"
echo "  - Screenshots: $(pwd)/reports/screenshots/"

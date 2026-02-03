# Makefile for Spark + Gemini AI Home Lab
# Simplifies common Docker Compose operations

.PHONY: help setup start stop restart logs status clean verify

# Default target
help:
	@echo "Spark + Gemini AI Home Lab - Available Commands"
	@echo ""
	@echo "  make setup     - Initial setup (run once)"
	@echo "  make start     - Start all services"
	@echo "  make stop      - Stop all services"
	@echo "  make restart   - Restart all services"
	@echo "  make logs      - View logs from all services"
	@echo "  make status    - Check status of services"
	@echo "  make verify    - Verify installation"
	@echo "  make clean     - Stop and remove containers"
	@echo ""
	@echo "Service-specific logs:"
	@echo "  make logs-spark-master"
	@echo "  make logs-spark-worker"
	@echo "  make logs-jupyter"
	@echo ""
	@echo "Quick access:"
	@echo "  make jupyter   - Open Jupyter in browser"
	@echo "  make spark-ui  - Open Spark UI in browser"
	@echo ""

# Initial setup
setup:
	@echo "Running initial setup..."
	@chmod +x scripts/setup.sh scripts/verify.sh
	@./scripts/setup.sh

# Start services
start:
	@echo "Starting all services..."
	@docker compose up -d
	@echo ""
	@echo "Services started! Access:"
	@echo "  - Jupyter Lab: http://localhost:8888"
	@echo "  - Spark Master: http://localhost:8080"
	@echo "  - Spark Worker: http://localhost:8081"

# Stop services
stop:
	@echo "Stopping all services..."
	@docker compose stop

# Restart services
restart:
	@echo "Restarting all services..."
	@docker compose restart

# View logs
logs:
	@docker compose logs -f

# Service-specific logs
logs-spark-master:
	@docker compose logs -f spark-master

logs-spark-worker:
	@docker compose logs -f spark-worker

logs-jupyter:
	@docker compose logs -f jupyter

# Check status
status:
	@echo "Service Status:"
	@docker compose ps
	@echo ""
	@echo "Docker Resources:"
	@docker stats --no-stream spark-master spark-worker jupyter-spark 2>/dev/null || echo "Containers not running"

# Verify installation
verify:
	@./scripts/verify.sh

# Clean up
clean:
	@echo "Stopping and removing containers..."
	@docker compose down
	@echo "Cleanup complete"

# Clean everything including volumes
clean-all:
	@echo "WARNING: This will delete all data in volumes!"
	@read -p "Are you sure? [y/N] " -n 1 -r; \
	echo; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		docker compose down -v; \
		echo "All containers and volumes removed"; \
	fi

# Open Jupyter in browser
jupyter:
	@echo "Opening Jupyter Lab..."
	@open http://localhost:8888 2>/dev/null || xdg-open http://localhost:8888 2>/dev/null || echo "Please open: http://localhost:8888"

# Open Spark UI in browser
spark-ui:
	@echo "Opening Spark Master UI..."
	@open http://localhost:8080 2>/dev/null || xdg-open http://localhost:8080 2>/dev/null || echo "Please open: http://localhost:8080"

# Run example script
example:
	@echo "Running example script..."
	@docker exec -it jupyter-spark python /home/jovyan/scripts/spark_gemini_example.py

# Enter Jupyter container shell
shell-jupyter:
	@docker exec -it jupyter-spark bash

# Enter Spark Master container shell
shell-spark:
	@docker exec -it spark-master bash

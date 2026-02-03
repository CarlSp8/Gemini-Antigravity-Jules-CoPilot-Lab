<div align="center">

<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />

  <h1>Spark + Gemini AI CoPilot Home Lab</h1>

  <p>Local development environment for Apache Spark with Google Gemini AI integration</p>

  <a href="https://aistudio.google.com/apps">Get Gemini API Key</a> • 
  <a href="#quick-start">Quick Start</a> • 
  <a href="#features">Features</a>

</div>

---

## 🚀 Overview

This repository provides a complete **open-source, MIT-licensed** home lab setup for experimenting with Apache Spark and Google Gemini AI. Perfect for developers using **Copilot Pro+** to build data processing pipelines enhanced with AI capabilities.

### What's Included

- 🐳 **Docker Compose** configuration for Spark cluster (master + worker)
- 📓 **Jupyter Lab** environment with PySpark pre-configured
- 🤖 **Gemini AI** integration examples and templates
- 📚 Sample notebooks demonstrating Spark + AI workflows
- ⚙️ Easy setup scripts for quick deployment

## ✨ Features

- **Spark 3.5** cluster with master and worker nodes
- **Jupyter Lab** for interactive development
- **Localhost access** to all services
- **Volume mounting** for persistent data and notebooks
- **Google AI Studio** integration ready
- **Experimental PDH level** toolkit support
- **MIT License** - free for personal and commercial use

## 📋 Prerequisites

- Docker & Docker Compose installed
- 4GB+ RAM available for containers
- Google AI API key (optional, for Gemini integration)
  - Get yours at: https://aistudio.google.com/

## 🏃 Quick Start

> **New to this?** Check out our [Quick Start Guide](QUICKSTART.md) for a step-by-step walkthrough!

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/CarlSp8/Gemini-Antigravity-Jules-CoPilot-Lab.git
cd Gemini-Antigravity-Jules-CoPilot-Lab

# Run the setup script
chmod +x scripts/setup.sh
./scripts/setup.sh

# OR use make (if available)
make setup
```

### 2. Configure Environment

Edit the `.env` file with your settings:

```bash
# Copy the example and edit
cp .env.example .env
# Edit .env and add your Google AI API key
```

### 3. Start the Environment

```bash
# Start all services (use 'docker compose' for V2, or 'docker-compose' for V1)
docker compose up -d

# Check logs
docker compose logs -f

# OR use make
make start
```

### 4. Access the Services

- **Spark Master UI**: http://localhost:8080
- **Spark Worker UI**: http://localhost:8081  
- **Jupyter Lab**: http://localhost:8888
- **Spark Master**: spark://localhost:7077

## 📚 Usage Examples

### Using Jupyter Lab

1. Open http://localhost:8888 in your browser
2. Navigate to `notebooks/spark_gemini_demo.ipynb`
3. Run the cells to see Spark + Gemini AI in action

### Running Python Scripts

```bash
# Execute the example script
docker exec -it jupyter-spark python /home/jovyan/scripts/spark_gemini_example.py
```

### Submitting Spark Jobs

```bash
# Submit to the Spark cluster
docker exec -it spark-master spark-submit \
  --master spark://spark-master:7077 \
  /scripts/spark_gemini_example.py
```

## 🗂️ Project Structure

```
.
├── docker-compose.yml      # Docker services configuration
├── .env.example           # Environment variables template
├── .gitignore            # Git ignore rules
├── LICENSE               # MIT License
├── README.md             # This file
├── data/                 # Data directory (mounted in containers)
├── notebooks/            # Jupyter notebooks
│   └── spark_gemini_demo.ipynb
└── scripts/              # Python scripts and utilities
    ├── setup.sh
    └── spark_gemini_example.py
```

## 🔧 Configuration

### Spark Configuration

Modify `docker-compose.yml` to adjust Spark settings:

- **Worker Memory**: `SPARK_WORKER_MEMORY=2G`
- **Worker Cores**: `SPARK_WORKER_CORES=2`
- **Executor Memory**: Set in your Spark code

### Gemini AI Integration

1. Get API key from https://aistudio.google.com/
2. Add to `.env`: `GOOGLE_AI_API_KEY=your-key-here`
3. Install SDK in Jupyter: `pip install google-generativeai`

## 🛠️ Development Workflow

### For Copilot Pro+ Users

This environment is optimized for AI-assisted development:

1. **Explore**: Use Jupyter notebooks for interactive experimentation
2. **Develop**: Write Spark jobs with Copilot assistance
3. **Test**: Run jobs locally before deploying to production
4. **Integrate**: Combine Spark data processing with Gemini AI

### Common Commands

```bash
# Using Docker Compose (V2 syntax recommended, V1 with hyphen also works)
docker compose up -d              # Start services
docker compose down               # Stop services
docker compose logs -f            # View logs
docker compose restart            # Restart services
docker exec -it [container] [cmd] # Execute command

# OR use the Makefile for convenience (handles both V1 and V2)
make start                        # Start all services
make stop                         # Stop all services
make logs                         # View all logs
make status                       # Check service status
make verify                       # Verify installation
make example                      # Run example script
make help                         # Show all available commands
```

## 📖 Learning Resources

- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Google AI Studio](https://aistudio.google.com/apps)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [PySpark Tutorial](https://spark.apache.org/docs/latest/api/python/)

## 🐛 Troubleshooting

### Containers won't start

```bash
# Check Docker is running
docker ps

# Check logs for errors
docker compose logs
```

### Can't connect to Spark

- Ensure all containers are running: `docker compose ps`
- Check Spark Master UI at http://localhost:8080
- Verify worker is connected to master

### Jupyter token not working

- Check `.env` file for `JUPYTER_TOKEN`
- Find token in logs: `docker compose logs jupyter`

## 🤝 Contributing

Contributions are welcome! This is an open-source project under the MIT License.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

Free for personal, educational, and commercial use in your home lab or production environments.

## 🌟 Acknowledgments

- Built with [Google AI Studio](https://aistudio.google.com/apps)
- Powered by [Apache Spark](https://spark.apache.org/)
- Optimized for [GitHub Copilot](https://github.com/features/copilot) development

---

<div align="center">
  <p>Made with ❤️ for the home lab community</p>
  <p><a href="https://aistudio.google.com/apps">Get Started with Gemini AI</a></p>
</div>

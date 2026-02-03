# Quick Start Guide

This guide will help you get your Spark + Gemini AI home lab up and running in minutes.

## Prerequisites Check

Before starting, ensure you have:

- [ ] Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- [ ] 4GB+ free RAM
- [ ] 10GB+ free disk space
- [ ] (Optional) Google AI API key from [AI Studio](https://aistudio.google.com/)

## 3-Minute Setup

### Step 1: Initial Setup (1 min)

```bash
# Make setup script executable
chmod +x scripts/setup.sh

# Run setup
./scripts/setup.sh
```

This will:
- ✅ Check Docker installation
- ✅ Create `.env` file from template
- ✅ Pull required Docker images

### Step 2: Configure (30 seconds)

Edit the `.env` file:

```bash
# Open in your favorite editor
nano .env
# or
vim .env
# or
code .env
```

**Minimum changes:**
- Set a secure `JUPYTER_TOKEN` for notebook access

**Optional (for AI features):**
- Add your `GOOGLE_AI_API_KEY` from https://aistudio.google.com/

### Step 3: Launch (30 seconds)

```bash
# Start all services
docker compose up -d

# Verify services are running
docker compose ps
```

You should see 3 containers running:
- `spark-master`
- `spark-worker`
- `jupyter-spark`

### Step 4: Access & Explore (1 min)

Open your browser and visit:

1. **Jupyter Lab**: http://localhost:8888
   - Use the token from your `.env` file
   - Open `notebooks/spark_gemini_demo.ipynb`
   - Run the cells to test everything

2. **Spark Master UI**: http://localhost:8080
   - See cluster status
   - Monitor running jobs

3. **Spark Worker UI**: http://localhost:8081
   - Check worker health
   - View resource usage

## First Commands

### In Jupyter Lab

Open a new Python notebook and try:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("HelloSpark") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

# Create test data
data = [("Hello", 1), ("Spark", 2), ("World", 3)]
df = spark.createDataFrame(data, ["text", "id"])
df.show()

spark.stop()
```

### From Command Line

```bash
# Run example script
docker exec -it jupyter-spark \
    python /home/jovyan/scripts/spark_gemini_example.py

# Submit a Spark job
docker exec -it spark-master \
    spark-submit --master spark://spark-master:7077 \
    /scripts/spark_gemini_example.py
```

## Next Steps

1. 📚 **Learn**: Check out the sample notebook in `notebooks/`
2. 🔧 **Customize**: Modify `docker-compose.yml` for your needs
3. 📊 **Experiment**: Create your own data processing pipelines
4. 🤖 **AI Integration**: Add Gemini AI to enhance your workflows

## Common Issues

### Can't access Jupyter?

```bash
# Get the token from logs
docker compose logs jupyter | grep token
```

### Containers not starting?

```bash
# Check logs for errors
docker compose logs

# Restart services
docker compose restart
```

### Low on resources?

Edit `docker-compose.yml` to reduce worker resources:

```yaml
SPARK_WORKER_MEMORY=1G  # Reduce from 2G
SPARK_WORKER_CORES=1    # Reduce from 2
```

## Stopping and Cleaning Up

```bash
# Stop all services
docker compose down

# Stop and remove volumes (data will be lost!)
docker compose down -v

# Remove downloaded images (to free space)
docker compose down --rmi all
```

## Help & Support

- 📖 Full documentation in [README.md](README.md)
- 🐛 Report issues on GitHub
- 💡 Share your projects with the community

---

**Ready to build? Let's go! 🚀**

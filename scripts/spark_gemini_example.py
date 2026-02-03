#!/usr/bin/env python3
"""
Spark Gemini AI Integration Example
Demonstrates integration between Apache Spark and Google AI Studio (Gemini)
"""

from pyspark.sql import SparkSession
import os

def create_spark_session():
    """Create and configure Spark session"""
    spark = SparkSession.builder \
        .appName("Gemini-Spark-Integration") \
        .master("spark://spark-master:7077") \
        .config("spark.executor.memory", "1g") \
        .getOrCreate()
    
    return spark

def example_data_processing(spark):
    """Example data processing with Spark"""
    # Create sample data
    data = [
        ("Data processing with Spark", 1),
        ("AI integration with Gemini", 2),
        ("Home lab setup complete", 3)
    ]
    
    columns = ["description", "id"]
    df = spark.createDataFrame(data, columns)
    
    # Show data
    print("\n=== Sample Data ===")
    df.show()
    
    # Perform some transformations
    print("\n=== Transformed Data ===")
    df.selectExpr("upper(description) as description", "id").show()
    
    return df

def main():
    """Main execution"""
    print("Starting Spark with Gemini AI Studio Integration...")
    
    # Create Spark session
    spark = create_spark_session()
    
    print(f"Spark Version: {spark.version}")
    print(f"Spark Master: {spark.sparkContext.master}")
    
    # Process example data
    df = example_data_processing(spark)
    
    # Note: For Gemini AI integration, use the Google AI Python SDK
    # with your API key from https://aistudio.google.com/
    api_key = os.getenv('GOOGLE_AI_API_KEY')
    if api_key and api_key != 'your-api-key-here':
        print("\n✓ Google AI API Key configured")
        print("You can now integrate Gemini AI models with your Spark workflows")
    else:
        print("\n! Set GOOGLE_AI_API_KEY in .env to enable Gemini AI integration")
        print("  Get your API key from: https://aistudio.google.com/")
    
    # Stop Spark session
    spark.stop()
    print("\nSpark session stopped successfully")

if __name__ == "__main__":
    main()

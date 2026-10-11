# Assignment 39: GenAI App Deployment

This repository contains the deployment files and platform comparisons for a Generative AI Streamlit application.

## Task 3: Compare Deployment Platforms

### 1. Streamlit Cloud vs Hugging Face Spaces
- **Streamlit Cloud:** Specifically optimized for deploying Streamlit python apps directly from GitHub repositories with minimal configuration.
- **Hugging Face Spaces:** A versatile platform supporting Streamlit, Gradio, and Docker, deeply integrated with the Hugging Face ecosystem for machine learning models.

### 2. Pros & Cons of Each
- **Streamlit Cloud:**
  - *Pros:* Extremely fast setup, seamless GitHub integration, free hosting for public apps.
  - *Cons:* Limited control over heavy backend server configurations, resource constraints on free tiers.
- **Hugging Face Spaces (Streamlit):**
  - *Pros:* Excellent for hosting ML models with hardware upgrades (CPU/GPU), great community reach.
  - *Cons:* Slightly steeper initial configuration for repository syncing.

### 3. When to Use Which
- Use **Streamlit Cloud** for rapid prototyping, data dashboards, and straightforward GenAI web interfaces.
- Use **Hugging Face Spaces** when your app requires heavy local model weights, custom Docker containers, or integration with Hugging Face model hubs.
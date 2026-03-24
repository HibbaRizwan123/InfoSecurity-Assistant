# 🔐 InfoSecurity Assistant
InfoSecurity Assistant is a RAG-based question answer application designed to answer questions based on my *University Information Security Coursework*.

## 🎯 Problem Statement
Information Security is a theoratical subject where concepts are spread across *multiple files*. Whenever I needed to find information about a specific topic,
I had to manually search through *different course files* one by one which was extremely time-consuming and inefficient.

## 💡 Problem Solution
To cater this problem, I have developed a RAG-based question & answer application named **InfoSecurity Assistant** which act as an intelligent study companion that instantly retrieves and answers questions from all 
course materials at once saving time and making studying more efficient by keeping my notes as primary source. I used a hybrid approach to answer any question **e.g., if user asked question from a topic that is briefly explained in my notes my application will be able to explain it in more detail**.

## ✨ Features
- 💬 Ask questions through a clean chat interface
- 📚 Answers are generated from course material
- 🔍 Retrieves the most relevant content using vector search
- ⚡ Powered by Google Gemini API for intelligent responses
- 🗄️ ChromaDB used as a local vector database

## 🛠️ Tech Stack
- ***Python*** : Core programming language
- ***Streamlit*** : Frontend chat interface
- ***LangChain*** : RAG pipeline framework 
- ***Google Gemini API*** : LLM for generating answers 
- ***ChromaDB*** : Vector database for document storage
- ***all-MiniLM-L6-v2*** : For creating embeddings

## 🧠 Working
1. ***Ingestion*** : PDFs are loaded, split into chunks and stored in ChromaDB
2. ***Retrieval*** : User question is converted to embeddings and similar chunks are retrieved
3. ***Generation*** : Retrieved chunks + question are sent to Gemini API
4. ***Response*** : Answer is displayed in the Streamlit chat interface

## 🔑 Environment Variables
`GEMINI_API_KEY` =Your Google Gemini API key 

## ⚠️ Note
This app is designed to answer questions **only from the Information Security course materials (Week 1 - Week 8)**. Questions outside this scope may not be answered accurately.

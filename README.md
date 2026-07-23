# MedTech Quality Management System (QMS): Automated Maintenance Pipeline

## 1. Objective
This project demonstrates an end-to-end data engineering and business intelligence pipeline for tracking medical device maintenance, failures, and operational uptime. The system is designed with regulatory traceability and enterprise security protocols in mind.

## 2. System Architecture & Data Lineage
* **Data Source:** Raw failure logs and maintenance records (CSV).
* **Processing Engine:** Python (Pandas) automated script.
* **Visualization & Analytics:** Microsoft Power BI.
* **Security Model:** Row-Level Security (RLS) deployed via DAX.

## 3. Data Transformation Logic (Python)
To ensure clean data enters the reporting environment, a Python script processes the raw logs.
* **Cleansing:** Automatically removes records missing critical compliance metrics (Age, Failure Count).
* **Feature Engineering:** Calculates a proprietary `Risk_Score` to prioritize maintenance schedules.
  * *Formula applied:* `(Age * 1.5) + (Failure_Event_Count * 3)`
* **Categorization:** Tags equipment as `High Risk`, `Moderate Risk`, or `Low Risk` based on the engineered score.

## 4. Enterprise Security (Access Control)
Strict data governance is enforced using Power BI Row-Level Security (RLS). 
* Vendor managers are restricted to viewing only their proprietary equipment. 
* *Example Logic deployed:* `[Manufacturer] = "CardioSync"` limits the dashboard view for external vendor audits.

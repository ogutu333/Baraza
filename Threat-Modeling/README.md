# AutoDrive STRIDE Threat Model Analysis

## Overview

This project presents a comprehensive **STRIDE threat model analysis** for AutoDrive Manufacturing's connected vehicle platform. The report evaluates the security posture of the platform by identifying potential threats, assessing their risks, and recommending mitigation strategies based on industry best practices.

The analysis focuses on protecting critical cloud-connected automotive systems that support secure authentication, telemetry management, Over-the-Air (OTA) software updates, secure messaging, and third-party API integrations.

---

## Objectives

- Analyze the security architecture of the connected vehicle platform.
- Identify threats using the STRIDE threat modeling framework.
- Assess the likelihood and impact of identified threats.
- Prioritize security risks based on their severity.
- Recommend mitigation strategies to strengthen the platform's security posture.

---

## STRIDE Framework

The report evaluates threats across the six STRIDE categories:

- **Spoofing** – Impersonating legitimate users, vehicles, or services.
- **Tampering** – Unauthorized modification of data or software.
- **Repudiation** – Denying actions due to insufficient logging or auditing.
- **Information Disclosure** – Exposure of confidential or sensitive information.
- **Denial of Service (DoS)** – Preventing legitimate access to system resources.
- **Elevation of Privilege** – Gaining unauthorized access to higher privilege levels.

---

## System Components Analyzed

The following components were included in the threat model:

- Vehicle Authentication System
- Vehicle Telemetry and Data Management
- Over-the-Air (OTA) Software Update System
- Secure Messaging and Communication System
- Third-Party API Integration

---

## Security Analysis

The report includes:

- System overview and scope
- Component-by-component security analysis
- STRIDE threat identification
- Risk assessment and prioritization
- Recommended mitigation strategies
- Summary of critical risks and security recommendations

---

## Technologies and Security Standards

- Amazon Web Services (AWS)
- AES-256 Encryption
- TLS 1.2 / TLS 1.3
- OAuth 2.0
- Multi-Factor Authentication (MFA)
- AWS Identity and Access Management (IAM)
- AWS CloudTrail
- AWS CloudWatch
- AWS GuardDuty
- AWS Web Application Firewall (WAF)
- AWS Shield Advanced
- AWS Secrets Manager
- ISO/SAE 21434 Road Vehicles – Cybersecurity Engineering

---

## Repository Structure

```text
.
├── README.md
├── STRIDE_Threat_Model_Analysis.md
├── Instructions.md
└── Scenario.md
```

---

## Files

| File | Description |
|------|-------------|
| **README.md** | Overview of the project, objectives, technologies used, and repository structure. |
| **STRIDE-Threat-Model-Analysis.md** | The completed STRIDE threat modeling report, including threat identification, risk assessment, mitigation strategies, and recommendations. |
| **instructions.md** | The lab requirements and tasks completed as part of the project. |
| **scenario.md** | Background information describing AutoDrive Manufacturing, the connected vehicle platform, and the system components analyzed. |

---

## Learning Outcomes

This project demonstrates practical understanding of:

- Threat modeling methodologies
- STRIDE security analysis
- Risk assessment techniques
- Cloud security concepts
- Automotive cybersecurity
- Security control selection
- Security documentation and reporting

---

## License

This project was provided by Moringa School.

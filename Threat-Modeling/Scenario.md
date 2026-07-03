# Lab: Threat Modeling

## Scenario

You have been hired as a cybersecurity analyst for **AutoDrive Manufacturing**, a leading automotive company specializing in connected and autonomous vehicle technology. AutoDrive develops smart vehicle systems that integrate cloud-based telemetry, remote diagnostics, and over-the-air (OTA) software updates to improve vehicle safety and performance.

The company relies on a secure infrastructure hosted on **Amazon Web Services (AWS)** to manage vehicle data, control remote software updates, and enable advanced driver assistance systems (ADAS).

Given the critical nature of automotive safety and compliance with industry standards such as **ISO/SAE 21434 (Road Vehicles – Cybersecurity Engineering)**, AutoDrive must protect its systems from cyber threats.

Recently, AutoDrive has experienced several security incidents, including:

- Unauthorized access attempts
- API abuse
- Firmware tampering
- Denial-of-Service (DoS) attacks

The company is conducting a **threat modeling analysis using the STRIDE framework** to identify potential security threats, evaluate risks, and implement mitigation strategies.

Your task is to analyze AutoDrive's security posture and document your findings using the provided report template.

---

# System Overview and Key Components

## 1. Vehicle Authentication System

- Vehicles authenticate to AutoDrive's cloud platform using digital certificates and secure key exchange mechanisms.
- Remote access to vehicle diagnostics requires **Multi-Factor Authentication (MFA)** for authorized personnel.
- A password reset process is available for registered users managing fleet services.

---

## 2. Vehicle Telemetry and Data Management

Each vehicle continuously transmits data including:

- Engine diagnostics
- Vehicle location
- Performance metrics

The data is stored in AutoDrive's cloud-based database.

### Security Controls

- Data encrypted at rest using **AES-256**
- Data encrypted in transit using **TLS 1.2/1.3**
- Only authorized AutoDrive engineers and fleet managers can access real-time telemetry data.

---

## 3. Over-the-Air (OTA) Software Update System

AutoDrive remotely deploys firmware updates to vehicles to:

- Patch vulnerabilities
- Improve vehicle performance

### Security Controls

- Firmware integrity verified using cryptographic signatures before installation.
- Update rollback capability is available in case of update failure or security concerns.

---

## 4. Secure Messaging and Communication System

Vehicles communicate securely with AutoDrive's cloud platform for:

- Software updates
- Emergency alerts
- Security warnings

### Security Controls

- All communications are encrypted.
- Anomalous message patterns are logged and monitored for potential cyber threats.

---

## 5. API for Third-Party Integration

AutoDrive provides a REST API that allows authorized service centers and partners to:

- Access vehicle diagnostics
- Retrieve security logs
- Retrieve software version details
- Request software updates for specific vehicle models

### Security Controls

- OAuth-based authentication
- API keys
- Rate limiting to prevent abuse

---

# Security Concerns and Threat Landscape

Recent cybersecurity concerns identified at AutoDrive Manufacturing include:

## Unauthorized Access Attempts

- Multiple failed login attempts from unknown locations.
- Indicates potential credential stuffing attacks.

## API Abuse

- Security logs reveal irregular API traffic.
- Suggests an attacker may be probing for vulnerabilities.

## Firmware Tampering

- Anomalous firmware version mismatches detected in vehicle logs.

## Denial-of-Service (DoS) Attempts

- Cloud authentication services experienced traffic spikes.
- Vehicle connectivity became overwhelmed.

## Data Leakage Risks

- API misconfigurations could expose sensitive vehicle telemetry data.

---
-- Hosts table
CREATE TABLE IF NOT EXISTS hosts (
  id SERIAL PRIMARY KEY,
  hostname VARCHAR(100) NOT NULL UNIQUE,
  ip_address INET NOT NULL,
  os_distribution VARCHAR(50),
  falcon_status VARCHAR(20) DEFAULT 'Unknown',
  falcon_version VARCHAR(20),
  is_reachable BOOLEAN DEFAULT true,
  owner_name VARCHAR(100),
  owner_email VARCHAR(100),
  last_seen TIMESTAMP DEFAULT NOW(),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
-- Alerts table
CREATE TABLE IF NOT EXISTS alerts (
  id SERIAL PRIMARY KEY,
  host_id INTEGER REFERENCES hosts(id),
  alert_type VARCHAR(20) NOT NULL,
  severity VARCHAR(10) NOT NULL,
  message TEXT NOT NULL,
  status VARCHAR(20) DEFAULT 'open',
  created_at TIMESTAMP DEFAULT NOW(),
  acknowledged_at TIMESTAMP,
  resolved_at TIMESTAMP
);
-- Anomalies table
CREATE TABLE IF NOT EXISTS anomalies (
  id SERIAL PRIMARY KEY,
  host_id INTEGER REFERENCES hosts(id),
  anomaly_score DECIMAL(4,3),
  anomaly_type VARCHAR(50),
  features JSONB,
  detected_at TIMESTAMP DEFAULT NOW()
);

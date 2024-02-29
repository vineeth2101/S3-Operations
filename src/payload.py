def valid_payload_json_check():
    return {
        "component": "report",
        "componentUuid": "47a2ae72-43f2-11ed-9126-0a1fe8e83e67",
        "changeTicketId": "SECP-398",
        "projectVersion": "0.0.665-se-741-524580272",
        "scans": [
            {
                "kind": "TRIVY_SCAN_REPORT",
                "uri": "https://artifacts.anaplan-np.net/artifactory/anaplan-develop/com/anaplan/seceng/0.0.28/seceng-automation-demo-0.0.28-trivy.json",
            },
            {
                "kind": "SNYK_CODE_SCAN_SARIF",
                "uri": "https://artifacts.anaplan-np.net/artifactory/anaplan-develop/com/anaplan/seceng/slowcar/slowcar/0.0.661/security-scan-reports/slowcar-code-scan-results-0.0.661.sarif",
            },
        ],
    }
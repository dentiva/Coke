"""
Synthetic SLMG demo data — replaces DuckDB for the demo version.
Mirrors the structure and values we'd see from a real Nielsen RMS ingestion.
All numbers carefully chosen to showcase the analytical patterns the system detects.
"""

PERIODS = ["Feb 25", "Mar 25", "Feb 26", "Mar 26"]
CURRENT = "Mar 26"
LY      = "Mar 25"
PRIOR   = "Feb 26"

ZONES = ["SLMG Total", "East UP-1", "East UP-2", "Central UP", "West UP", "SLMG Bihar"]
TCCC_BRANDS = ["THUMS UP", "SPRITE", "COCA-COLA", "MAAZA", "KINLEY", "LIMCA", "FANTA", "MINUTE MAID"]
ALL_BRANDS  = TCCC_BRANDS + ["PEPSI", "MIRINDA", "7UP", "MOUNTAIN DEW", "CAMPA", "BISLERI", "FROOTI", "APPY"]

# ── PORTFOLIO SUMMARY per (period, zone) ─────────────────────────────────────
PORTFOLIO = {
    ("Mar 26", "SLMG Total"):  {"ms_value_pct": 52.6, "ms_volume_pct": 54.1, "avg_wd_pct": 74.0, "sppd": 129, "sah": 0.71, "rr": 0.92, "sots_pct": 51.8, "tccc_sales_value": 2845000},
    ("Feb 26", "SLMG Total"):  {"ms_value_pct": 53.4, "ms_volume_pct": 54.8, "avg_wd_pct": 74.5, "sppd": 127, "sah": 0.72, "rr": 0.94, "sots_pct": 52.6, "tccc_sales_value": 2782000},
    ("Mar 25", "SLMG Total"):  {"ms_value_pct": 53.1, "ms_volume_pct": 54.5, "avg_wd_pct": 74.5, "sppd": 126, "sah": 0.71, "rr": 0.95, "sots_pct": 52.3, "tccc_sales_value": 2698000},
    ("Feb 25", "SLMG Total"):  {"ms_value_pct": 53.8, "ms_volume_pct": 55.0, "avg_wd_pct": 75.0, "sppd": 125, "sah": 0.72, "rr": 0.96, "sots_pct": 52.9, "tccc_sales_value": 2645000},

    ("Mar 26", "East UP-1"):   {"ms_value_pct": 54.2, "ms_volume_pct": 55.8, "avg_wd_pct": 79.0, "sppd": 134, "sah": 0.69, "rr": 0.94, "sots_pct": 53.4, "tccc_sales_value": 612000},
    ("Mar 26", "East UP-2"):   {"ms_value_pct": 51.1, "ms_volume_pct": 52.6, "avg_wd_pct": 76.0, "sppd": 128, "sah": 0.67, "rr": 0.91, "sots_pct": 50.2, "tccc_sales_value": 498000},
    ("Mar 26", "Central UP"):  {"ms_value_pct": 51.8, "ms_volume_pct": 53.0, "avg_wd_pct": 74.0, "sppd": 131, "sah": 0.70, "rr": 0.93, "sots_pct": 51.1, "tccc_sales_value": 687000},
    ("Mar 26", "West UP"):     {"ms_value_pct": 53.9, "ms_volume_pct": 55.2, "avg_wd_pct": 71.0, "sppd": 127, "sah": 0.76, "rr": 0.95, "sots_pct": 53.0, "tccc_sales_value": 578000},
    ("Mar 26", "SLMG Bihar"):  {"ms_value_pct": 52.1, "ms_volume_pct": 53.4, "avg_wd_pct": 68.0, "sppd": 119, "sah": 0.77, "rr": 0.88, "sots_pct": 51.0, "tccc_sales_value": 470000},

    ("Mar 25", "East UP-1"):   {"ms_value_pct": 54.0, "ms_volume_pct": 55.6, "avg_wd_pct": 79.5, "sppd": 131, "sah": 0.68, "rr": 0.95, "sots_pct": 53.2, "tccc_sales_value": 588000},
    ("Mar 25", "East UP-2"):   {"ms_value_pct": 54.5, "ms_volume_pct": 55.9, "avg_wd_pct": 77.0, "sppd": 130, "sah": 0.71, "rr": 0.94, "sots_pct": 53.6, "tccc_sales_value": 542000},
    ("Mar 25", "Central UP"):  {"ms_value_pct": 52.2, "ms_volume_pct": 53.4, "avg_wd_pct": 74.5, "sppd": 128, "sah": 0.70, "rr": 0.94, "sots_pct": 51.4, "tccc_sales_value": 661000},
    ("Mar 25", "West UP"):     {"ms_value_pct": 53.7, "ms_volume_pct": 54.9, "avg_wd_pct": 71.5, "sppd": 124, "sah": 0.75, "rr": 0.96, "sots_pct": 52.8, "tccc_sales_value": 561000},
    ("Mar 25", "SLMG Bihar"):  {"ms_value_pct": 52.4, "ms_volume_pct": 53.6, "avg_wd_pct": 68.5, "sppd": 117, "sah": 0.77, "rr": 0.91, "sots_pct": 51.2, "tccc_sales_value": 455000},
}

# ── BRAND TRENDS — 4 periods × brands × zones ────────────────────────────────
BRAND_METRICS = {
    "THUMS UP": {
        "SLMG Total": [
            {"period": "Feb 25", "ms_value_pct": 29.1, "ms_volume_pct": 30.2, "wd_pct": 83.0, "sppd": 138, "sah": 0.35, "rr": 0.94, "sots_pct": 28.6},
            {"period": "Mar 25", "ms_value_pct": 28.5, "ms_volume_pct": 29.6, "wd_pct": 82.0, "sppd": 142, "sah": 0.35, "rr": 0.92, "sots_pct": 28.0},
            {"period": "Feb 26", "ms_value_pct": 27.8, "ms_volume_pct": 28.9, "wd_pct": 81.0, "sppd": 139, "sah": 0.34, "rr": 0.91, "sots_pct": 27.4},
            {"period": "Mar 26", "ms_value_pct": 27.2, "ms_volume_pct": 28.3, "wd_pct": 81.0, "sppd": 136, "sah": 0.34, "rr": 0.90, "sots_pct": 26.8},
        ],
        "East UP-2": [
            {"period": "Feb 25", "ms_value_pct": 31.2, "ms_volume_pct": 32.4, "wd_pct": 79.0, "sppd": 144, "sah": 0.39, "rr": 0.93, "sots_pct": 30.7},
            {"period": "Mar 25", "ms_value_pct": 30.8, "ms_volume_pct": 31.9, "wd_pct": 79.0, "sppd": 148, "sah": 0.39, "rr": 0.91, "sots_pct": 30.3},
            {"period": "Feb 26", "ms_value_pct": 28.9, "ms_volume_pct": 30.0, "wd_pct": 79.0, "sppd": 140, "sah": 0.37, "rr": 0.89, "sots_pct": 28.4},
            {"period": "Mar 26", "ms_value_pct": 26.7, "ms_volume_pct": 27.8, "wd_pct": 78.0, "sppd": 132, "sah": 0.34, "rr": 0.87, "sots_pct": 26.3},
        ],
        "Central UP": [
            {"period": "Feb 25", "ms_value_pct": 28.4, "ms_volume_pct": 29.5, "wd_pct": 80.0, "sppd": 135, "sah": 0.36, "rr": 0.93, "sots_pct": 28.0},
            {"period": "Mar 25", "ms_value_pct": 27.9, "ms_volume_pct": 29.0, "wd_pct": 79.0, "sppd": 138, "sah": 0.35, "rr": 0.91, "sots_pct": 27.5},
            {"period": "Feb 26", "ms_value_pct": 27.1, "ms_volume_pct": 28.2, "wd_pct": 78.0, "sppd": 133, "sah": 0.35, "rr": 0.90, "sots_pct": 26.7},
            {"period": "Mar 26", "ms_value_pct": 26.8, "ms_volume_pct": 27.9, "wd_pct": 78.0, "sppd": 131, "sah": 0.34, "rr": 0.89, "sots_pct": 26.4},
        ],
    },
    "SPRITE": {
        "SLMG Total": [
            {"period": "Feb 25", "ms_value_pct": 7.9, "ms_volume_pct": 8.1, "wd_pct": 72.0, "sppd": 94, "sah": 0.11, "rr": 0.86, "sots_pct": 7.8},
            {"period": "Mar 25", "ms_value_pct": 8.2, "ms_volume_pct": 8.4, "wd_pct": 74.0, "sppd": 98, "sah": 0.11, "rr": 0.84, "sots_pct": 8.1},
            {"period": "Feb 26", "ms_value_pct": 8.4, "ms_volume_pct": 8.6, "wd_pct": 75.0, "sppd": 101, "sah": 0.11, "rr": 0.83, "sots_pct": 8.3},
            {"period": "Mar 26", "ms_value_pct": 8.5, "ms_volume_pct": 8.7, "wd_pct": 74.0, "sppd": 98, "sah": 0.11, "rr": 0.79, "sots_pct": 8.4},
        ],
        "SLMG Bihar": [
            {"period": "Feb 25", "ms_value_pct": 7.1, "ms_volume_pct": 7.3, "wd_pct": 68.0, "sppd": 88, "sah": 0.10, "rr": 0.91, "sots_pct": 7.0},
            {"period": "Mar 25", "ms_value_pct": 7.4, "ms_volume_pct": 7.6, "wd_pct": 69.0, "sppd": 92, "sah": 0.11, "rr": 0.88, "sots_pct": 7.3},
            {"period": "Feb 26", "ms_value_pct": 7.2, "ms_volume_pct": 7.4, "wd_pct": 69.0, "sppd": 90, "sah": 0.10, "rr": 0.79, "sots_pct": 7.1},
            {"period": "Mar 26", "ms_value_pct": 7.0, "ms_volume_pct": 7.2, "wd_pct": 68.0, "sppd": 87, "sah": 0.10, "rr": 0.71, "sots_pct": 6.9},
        ],
    },
    "KINLEY": {
        "SLMG Total": [
            {"period": "Feb 25", "ms_value_pct": 11.8, "ms_volume_pct": 12.2, "wd_pct": 68.0, "sppd": 82, "sah": 0.17, "rr": 0.97, "sots_pct": 11.6},
            {"period": "Mar 25", "ms_value_pct": 12.3, "ms_volume_pct": 12.7, "wd_pct": 71.0, "sppd": 87, "sah": 0.17, "rr": 0.98, "sots_pct": 12.1},
            {"period": "Feb 26", "ms_value_pct": 12.8, "ms_volume_pct": 13.2, "wd_pct": 72.0, "sppd": 89, "sah": 0.18, "rr": 0.99, "sots_pct": 12.6},
            {"period": "Mar 26", "ms_value_pct": 13.1, "ms_volume_pct": 13.5, "wd_pct": 71.0, "sppd": 87, "sah": 0.18, "rr": 1.01, "sots_pct": 12.9},
        ],
        "West UP": [
            {"period": "Feb 25", "ms_value_pct": 14.2, "ms_volume_pct": 14.6, "wd_pct": 44.0, "sppd": 91, "sah": 0.32, "rr": 0.96, "sots_pct": 14.0},
            {"period": "Mar 25", "ms_value_pct": 14.8, "ms_volume_pct": 15.2, "wd_pct": 44.0, "sppd": 95, "sah": 0.34, "rr": 0.97, "sots_pct": 14.6},
            {"period": "Feb 26", "ms_value_pct": 15.1, "ms_volume_pct": 15.5, "wd_pct": 44.0, "sppd": 97, "sah": 0.34, "rr": 0.98, "sots_pct": 14.9},
            {"period": "Mar 26", "ms_value_pct": 15.6, "ms_volume_pct": 16.0, "wd_pct": 44.0, "sppd": 98, "sah": 0.35, "rr": 1.02, "sots_pct": 15.4},
        ],
    },
    "CAMPA": {
        "SLMG Total": [
            {"period": "Feb 25", "ms_value_pct": 5.2,  "ms_volume_pct": 5.4,  "wd_pct": 41.0, "sppd": 72, "sah": 0.13, "rr": 1.12, "sots_pct": 5.1},
            {"period": "Mar 25", "ms_value_pct": 5.8,  "ms_volume_pct": 6.0,  "wd_pct": 45.0, "sppd": 76, "sah": 0.13, "rr": 1.15, "sots_pct": 5.7},
            {"period": "Feb 26", "ms_value_pct": 6.4,  "ms_volume_pct": 6.6,  "wd_pct": 52.0, "sppd": 80, "sah": 0.12, "rr": 1.18, "sots_pct": 6.3},
            {"period": "Mar 26", "ms_value_pct": 7.2,  "ms_volume_pct": 7.5,  "wd_pct": 59.0, "sppd": 84, "sah": 0.12, "rr": 1.21, "sots_pct": 7.1},
        ],
        "Central UP": [
            {"period": "Feb 25", "ms_value_pct": 6.1,  "ms_volume_pct": 6.3,  "wd_pct": 48.0, "sppd": 78, "sah": 0.13, "rr": 1.14, "sots_pct": 6.0},
            {"period": "Mar 25", "ms_value_pct": 6.9,  "ms_volume_pct": 7.1,  "wd_pct": 54.0, "sppd": 82, "sah": 0.13, "rr": 1.17, "sots_pct": 6.8},
            {"period": "Feb 26", "ms_value_pct": 8.3,  "ms_volume_pct": 8.5,  "wd_pct": 63.0, "sppd": 88, "sah": 0.13, "rr": 1.22, "sots_pct": 8.2},
            {"period": "Mar 26", "ms_value_pct": 10.1, "ms_volume_pct": 10.4, "wd_pct": 71.0, "sppd": 94, "sah": 0.14, "rr": 1.28, "sots_pct": 10.0},
        ],
    },
    "COCA-COLA": {
        "SLMG Total": [
            {"period": "Feb 25", "ms_value_pct": 8.3, "ms_volume_pct": 8.5, "wd_pct": 76.0, "sppd": 109, "sah": 0.11, "rr": 0.95, "sots_pct": 8.2},
            {"period": "Mar 25", "ms_value_pct": 8.5, "ms_volume_pct": 8.7, "wd_pct": 77.0, "sppd": 110, "sah": 0.11, "rr": 0.96, "sots_pct": 8.4},
            {"period": "Feb 26", "ms_value_pct": 8.9, "ms_volume_pct": 9.1, "wd_pct": 78.0, "sppd": 114, "sah": 0.11, "rr": 0.97, "sots_pct": 8.8},
            {"period": "Mar 26", "ms_value_pct": 9.2, "ms_volume_pct": 9.4, "wd_pct": 78.0, "sppd": 118, "sah": 0.12, "rr": 0.98, "sots_pct": 9.1},
        ],
    },
    "MAAZA": {
        "SLMG Total": [
            {"period": "Feb 25", "ms_value_pct": 4.1, "ms_volume_pct": 4.3, "wd_pct": 58.0, "sppd": 71, "sah": 0.07, "rr": 0.99, "sots_pct": 4.0},
            {"period": "Mar 25", "ms_value_pct": 4.3, "ms_volume_pct": 4.5, "wd_pct": 59.0, "sppd": 73, "sah": 0.07, "rr": 1.00, "sots_pct": 4.2},
            {"period": "Feb 26", "ms_value_pct": 4.5, "ms_volume_pct": 4.7, "wd_pct": 60.0, "sppd": 75, "sah": 0.08, "rr": 1.01, "sots_pct": 4.4},
            {"period": "Mar 26", "ms_value_pct": 4.7, "ms_volume_pct": 4.9, "wd_pct": 61.0, "sppd": 77, "sah": 0.08, "rr": 1.02, "sots_pct": 4.6},
        ],
    },
    "LIMCA": {
        "SLMG Total": [
            {"period": "Feb 25", "ms_value_pct": 2.5, "ms_volume_pct": 2.6, "wd_pct": 55.0, "sppd": 45, "sah": 0.05, "rr": 0.92, "sots_pct": 2.5},
            {"period": "Mar 25", "ms_value_pct": 2.4, "ms_volume_pct": 2.5, "wd_pct": 54.0, "sppd": 44, "sah": 0.04, "rr": 0.91, "sots_pct": 2.4},
            {"period": "Feb 26", "ms_value_pct": 2.3, "ms_volume_pct": 2.4, "wd_pct": 53.0, "sppd": 43, "sah": 0.04, "rr": 0.90, "sots_pct": 2.3},
            {"period": "Mar 26", "ms_value_pct": 2.2, "ms_volume_pct": 2.3, "wd_pct": 52.0, "sppd": 42, "sah": 0.04, "rr": 0.89, "sots_pct": 2.2},
        ],
    },
    "FANTA": {
        "SLMG Total": [
            {"period": "Feb 25", "ms_value_pct": 3.8, "ms_volume_pct": 3.9, "wd_pct": 64.0, "sppd": 59, "sah": 0.06, "rr": 0.94, "sots_pct": 3.7},
            {"period": "Mar 25", "ms_value_pct": 3.7, "ms_volume_pct": 3.8, "wd_pct": 63.0, "sppd": 58, "sah": 0.06, "rr": 0.93, "sots_pct": 3.6},
            {"period": "Feb 26", "ms_value_pct": 3.6, "ms_volume_pct": 3.7, "wd_pct": 62.0, "sppd": 58, "sah": 0.06, "rr": 0.92, "sots_pct": 3.5},
            {"period": "Mar 26", "ms_value_pct": 3.5, "ms_volume_pct": 3.6, "wd_pct": 61.0, "sppd": 57, "sah": 0.06, "rr": 0.91, "sots_pct": 3.4},
        ],
    },
    "MINUTE MAID": {
        "SLMG Total": [
            {"period": "Feb 25", "ms_value_pct": 1.9, "ms_volume_pct": 2.0, "wd_pct": 48.0, "sppd": 40, "sah": 0.04, "rr": 0.95, "sots_pct": 1.9},
            {"period": "Mar 25", "ms_value_pct": 2.1, "ms_volume_pct": 2.2, "wd_pct": 50.0, "sppd": 42, "sah": 0.04, "rr": 0.96, "sots_pct": 2.0},
            {"period": "Feb 26", "ms_value_pct": 2.3, "ms_volume_pct": 2.4, "wd_pct": 52.0, "sppd": 44, "sah": 0.04, "rr": 0.98, "sots_pct": 2.2},
            {"period": "Mar 26", "ms_value_pct": 2.4, "ms_volume_pct": 2.5, "wd_pct": 53.0, "sppd": 45, "sah": 0.05, "rr": 0.99, "sots_pct": 2.3},
        ],
    },
    "PEPSI": {
        "SLMG Total": [
            {"period": "Feb 25", "ms_value_pct": 13.2, "ms_volume_pct": 13.5, "wd_pct": 74.0, "sppd": 114, "sah": 0.18, "rr": 0.93, "sots_pct": 13.1},
            {"period": "Mar 25", "ms_value_pct": 13.5, "ms_volume_pct": 13.8, "wd_pct": 74.0, "sppd": 117, "sah": 0.18, "rr": 0.94, "sots_pct": 13.4},
            {"period": "Feb 26", "ms_value_pct": 13.9, "ms_volume_pct": 14.2, "wd_pct": 75.0, "sppd": 119, "sah": 0.19, "rr": 0.95, "sots_pct": 13.8},
            {"period": "Mar 26", "ms_value_pct": 14.3, "ms_volume_pct": 14.7, "wd_pct": 75.0, "sppd": 122, "sah": 0.19, "rr": 0.96, "sots_pct": 14.2},
        ],
    },
}

# Fill in missing zones for each brand with SLMG Total values (slight variation)
for brand in BRAND_METRICS:
    slmg_data = BRAND_METRICS[brand].get("SLMG Total", [])
    for zone in ["East UP-1", "East UP-2", "Central UP", "West UP", "SLMG Bihar"]:
        if zone not in BRAND_METRICS[brand]:
            # Clone with slight variation (±10%)
            import random
            random.seed(hash(brand + zone))
            BRAND_METRICS[brand][zone] = [
                {**d,
                 "ms_value_pct":  round(d["ms_value_pct"]  * random.uniform(0.9, 1.1), 1),
                 "ms_volume_pct": round(d["ms_volume_pct"] * random.uniform(0.9, 1.1), 1),
                 "wd_pct":        round(d["wd_pct"]        * random.uniform(0.95, 1.05), 1),
                 "sppd":          round(d["sppd"]          * random.uniform(0.9, 1.1), 0),
                 "sah":           round(d["sah"]           * random.uniform(0.85, 1.15), 3),
                 "rr":            round(d["rr"]            * random.uniform(0.95, 1.05), 2),
                 "sots_pct":      round(d["sots_pct"]      * random.uniform(0.9, 1.1), 1),
                 }
                for d in slmg_data
            ]

# ── BRAND OWNER SHARE — for pie/bar chart ─────────────────────────────────────
BRAND_OWNER_SHARE = {
    ("Mar 26", "SLMG Total"):  [
        {"brand_owner": "TCCC",           "sales": 2845000, "ms_pct": 52.6},
        {"brand_owner": "PEPSICO",        "sales": 1249000, "ms_pct": 23.1},
        {"brand_owner": "PARLE AGRO",     "sales":  595000, "ms_pct": 11.0},
        {"brand_owner": "RELIANCE RETAIL","sales":  389000, "ms_pct":  7.2},
        {"brand_owner": "BISLERI INT'L",  "sales":  232000, "ms_pct":  4.3},
        {"brand_owner": "OTHERS",         "sales":  100000, "ms_pct":  1.8},
    ],
    ("Mar 25", "SLMG Total"):  [
        {"brand_owner": "TCCC",           "sales": 2698000, "ms_pct": 53.1},
        {"brand_owner": "PEPSICO",        "sales": 1133000, "ms_pct": 22.3},
        {"brand_owner": "PARLE AGRO",     "sales":  569000, "ms_pct": 11.2},
        {"brand_owner": "RELIANCE RETAIL","sales":  295000, "ms_pct":  5.8},
        {"brand_owner": "BISLERI INT'L",  "sales":  255000, "ms_pct":  5.0},
        {"brand_owner": "OTHERS",         "sales":  135000, "ms_pct":  2.6},
    ],
}

# ── ANOMALIES ─────────────────────────────────────────────────────────────────
ANOMALIES = [
    {
        "type":        "Leaky Bucket",
        "severity":    "HIGH",
        "brand":       "THUMS UP",
        "zone":        "East UP-2",
        "period":      "Mar 26",
        "description": "MS dropped 4.1pts over 4 months (31.2% → 26.7%). WD stable at 78-79%, but SAH falling from 0.39 to 0.34. Distribution is there but consumers not buying — classic leaky bucket symptom.",
        "action":      "Review price/pack proposition in Varanasi & Prayagraj. Check competitive activity from Pepsi and Campa. Consumer-level intervention needed.",
        "metrics":     {"ms_current": 26.7, "ms_prior": 31.2, "ms_drop": 4.5, "sah": 0.34, "wd": 78},
    },
    {
        "type":        "Competitor Surge",
        "severity":    "HIGH",
        "brand":       "CAMPA",
        "zone":        "Central UP",
        "period":      "Mar 26",
        "description": "Campa MS grew +3.2pts in a single month (Feb→Mar 26). WD jumped 8pts to 71%. Aggressive distribution push by Reliance Retail in Lucknow & Kanpur trade channels.",
        "action":      "Immediate field investigation in Lucknow/Kanpur. Assess trade terms being offered by Campa. Counter with TCCC trade schemes and enhanced cooler activation.",
        "metrics":     {"ms_current": 10.1, "ms_prior": 8.3, "ms_gain": 1.8, "wd": 71},
    },
    {
        "type":        "Replenishment Stress",
        "severity":    "HIGH",
        "brand":       "SPRITE",
        "zone":        "SLMG Bihar",
        "period":      "Mar 26",
        "description": "RR dropped to 0.71 in Mar 26 (critical threshold: 0.80). Chilled outlets at OOS risk. MS already showing early decline. Supply chain failing to match demand.",
        "action":      "Escalate to supply chain immediately. Prioritise Bihar depot replenishment. Field team audit of chilled availability across SLMG Bihar DDRs within 48 hrs.",
        "metrics":     {"rr": 0.71, "wd": 68, "ms": 7.0},
    },
    {
        "type":        "Hidden Gem",
        "severity":    "MEDIUM",
        "brand":       "KINLEY",
        "zone":        "West UP",
        "period":      "Mar 26",
        "description": "SAH of 0.35 with only 44% WD — extremely high velocity in the outlets that stock it. Significant untapped distribution opportunity.",
        "action":      "Expand WD in West UP (Bareilly & Doon zones first). Each +10pts WD at current SAH projects to +1.5pts MS gain.",
        "metrics":     {"sah": 0.35, "wd": 44, "ms": 15.6},
    },
    {
        "type":        "WD Quality Gap",
        "severity":    "MEDIUM",
        "brand":       "THUMS UP",
        "zone":        "SLMG Total",
        "period":      "Mar 26",
        "description": "DQI trending down from 1.21 to 1.19 over 4 months. WD declining while ND holds steady — Thums Up is losing presence in high-value outlets (the shops that drive category sales).",
        "action":      "Review key account coverage list. Ensure top-50 DDR outlets by category sales are not being de-listed. Protect high-throughput shelf space.",
        "metrics":     {"dqi": 1.19, "wd": 81, "ms": 27.2},
    },
    {
        "type":        "Dilution Signal",
        "severity":    "LOW",
        "brand":       "MAAZA",
        "zone":        "East UP-1",
        "period":      "Mar 26",
        "description": "WD expanding slightly (+1.5pts) but SPPD flat. New outlets added may not be matching existing outlet throughput.",
        "action":      "Monitor for 1 more period. If SPPD continues to underperform, pause expansion and focus on rotation improvement.",
        "metrics":     {"wd_gain": 1.5, "sppd": 77},
    },
]

# ── GEO SCORECARD ─────────────────────────────────────────────────────────────
GEO_SCORECARD = {
    "Mar 26": [
        {"zone": "East UP-1",  "period": "Mar 26", "ms_value_pct": 54.2, "avg_wd_pct": 79.0, "sppd": 134, "rr": 0.94},
        {"zone": "East UP-2",  "period": "Mar 26", "ms_value_pct": 51.1, "avg_wd_pct": 76.0, "sppd": 128, "rr": 0.91},
        {"zone": "Central UP", "period": "Mar 26", "ms_value_pct": 51.8, "avg_wd_pct": 74.0, "sppd": 131, "rr": 0.93},
        {"zone": "West UP",    "period": "Mar 26", "ms_value_pct": 53.9, "avg_wd_pct": 71.0, "sppd": 127, "rr": 0.95},
        {"zone": "SLMG Bihar", "period": "Mar 26", "ms_value_pct": 52.1, "avg_wd_pct": 68.0, "sppd": 119, "rr": 0.78},
        {"zone": "SLMG Total", "period": "Mar 26", "ms_value_pct": 52.6, "avg_wd_pct": 74.0, "sppd": 129, "rr": 0.92},
    ],
    "Feb 26": [
        {"zone": "East UP-1",  "period": "Feb 26", "ms_value_pct": 54.0, "avg_wd_pct": 79.0, "sppd": 131, "rr": 0.95},
        {"zone": "East UP-2",  "period": "Feb 26", "ms_value_pct": 52.5, "avg_wd_pct": 76.5, "sppd": 127, "rr": 0.92},
        {"zone": "Central UP", "period": "Feb 26", "ms_value_pct": 52.2, "avg_wd_pct": 74.5, "sppd": 129, "rr": 0.93},
        {"zone": "West UP",    "period": "Feb 26", "ms_value_pct": 54.0, "avg_wd_pct": 71.5, "sppd": 125, "rr": 0.95},
        {"zone": "SLMG Bihar", "period": "Feb 26", "ms_value_pct": 52.5, "avg_wd_pct": 68.5, "sppd": 118, "rr": 0.85},
        {"zone": "SLMG Total", "period": "Feb 26", "ms_value_pct": 53.4, "avg_wd_pct": 74.5, "sppd": 127, "rr": 0.94},
    ],
}

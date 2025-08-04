## Setup

```bash
python3 -m venv venv_parametrix
source venv_parametrix/bin/activate
pip install -r env/requirements.txt
```



# Parametrix System Pipeline: Full Logic Flow

This document describes the full data and computation flow of the Parametrix system, from ingestion to final outputs.

---

## 1. SATELLITE + WEATHER INGESTION

**Inputs**  
- Sentinel-2, MODIS, SMAP satellite data  
- ERA5 and GFS weather datasets  

**Transformations and Modules**

```
sentinel_ndvi_downloader.py
    ↓
cloud_masker.py
    ↓
ndvi_normalizer.py
    ↓
ndvi_gap_filler.py
    ↓
static_feature_generator.py

era5_weather_fetcher.py
    ↓
elevation_resampler.py
    ↓
soil_data_loader.py

gfs_forecast_ingestor.py
```

**Outputs**  
- NDVI arrays  
- ERA5 tensors  
- GFS forecasts  
- Static land features

---

## 2. MODELING & FORECASTING

**Inputs**  
- Preprocessed NDVI  
- ERA5/GFS tensors  
- Static feature grid  

**Transformations and Modules**

```
transformer_forecaster.py
    ↓
crop_yield_regressor.py / coffee_yield_predictor.py
    ↓
bayesian_uncertainty_model.py
    ↓
value_at_risk_simulator.py

multi_model_blender.py ⇄ lstm_ndvi_predictor.py
                         ddpm_era5_upsampler.py
                         gpp_proxy_estimator.py
                         timeseries_fusion_model.py
                         ensemble_selector.py
```

**Outputs**  
- Yield predictions  
- Confidence intervals  
- VaR/CVaR profiles

---

## 3. TRIGGERING

**Transformations and Modules**

```
threshold_trigger_engine.py
    ↓
region_trigger_fusion.py
    ↓
multi-trigger_resolver.py
    ↓
trigger_validation_scanner.py
    ↓
contract_logic_evaluator.py

Special triggers:
irrigation_trigger_scanner.py
fertilizer_timing_trigger.py
subsidy_burn_optimizer.py
forecast_window_adjuster.py
contract_auto_calibrator.py
```

**Outputs**  
- Trigger decision  
- Severity/confidence  
- Historical validation

---

## 4. CONTRACTS & DISBURSEMENT

**Transformations and Modules**

```
smart_contract_emitter.py
    ↓
oracle_json_generator.py
    ↓
chainlink_oracle_uploader.py
    ↓
trigger_receipt_hash_generator.py
    ↓
pdf_bundle_generator.py
    ↓
offline_bundle_exporter.py
```

**Outputs**  
- PDF payout bundle  
- JSON oracle update  
- Smart contract payload

---

## 5. LOCAL OUTPUT DELIVERY

**Modules**

```
mobile_sms_generator.py
regional_language_renderer.py
qr_payload_encoder.py
whatsapp_audio_summary.py
mobile_ui_bundle_exporter.py
```

**Outputs**  
- Localized SMS, voice, QR  
- Offline-accessible JSONs

---

## 6. VALIDATION & SIMULATION

**Modules**

```
spatial_bias_audit.py
model_benchmark_suite.py
ground_truth_validator.py
dispute_simulator.py
verifiability_index_calculator.py
conflict_trigger_resolver.py
trigger_audit_logger.py
```

**Outputs**  
- Fairness reports  
- Simulation artifacts  
- Compliance logs

---

## 7. ORCHESTRATION

**Driver Modules**

```
trigger_pipeline_orchestrator.py
    ↓
cli_runner.py
api_server.py
notebooks/
demo_config_loader.py
```

**Final Outputs**  
- Run outputs  
- API results  
- Logs and bundles

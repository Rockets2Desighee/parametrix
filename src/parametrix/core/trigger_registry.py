from parametrix.triggers import (
    contract_auto_calibrator,
    contract_logic_evaluator,
    fertilizer_timing_trigger,
    irrigation_trigger_scanner,
    monte_carlo_trigger_simulator,
    multi_trigger_resolver,
    region_trigger_fusion,
    subsidy_burn_optimizer,
    threshold_trigger_engine,
    trigger_validation_scanner,
)

from parametrix.domains.climate_extremes import (
    flash_drought,
    compound_event_trigger,
    frost_trigger,
)

from parametrix.domains.infrastructure import (
    road_accessibility_score,
    grid_overload_trigger,
    communication_risk_proxy,
)

from parametrix.domains.dao_triggers import (
    disbursement_delay_fallback,
    macro_fiscal_trigger,
    pricing_recalibration_engine,
)

TRIGGER_REGISTRY = {
    # Core
    "threshold": threshold_trigger_engine.ThresholdTriggerEngine,
    "irrigation": irrigation_trigger_scanner.IrrigationTriggerScanner,
    "fertilizer": fertilizer_timing_trigger.FertilizerTimingTrigger,
    "contract_logic": contract_logic_evaluator.ContractLogicEvaluator,

    # Climate
    "frost": frost_trigger.FrostTrigger,
    "flash_drought": flash_drought.FlashDroughtTrigger,
    "compound_event": compound_event_trigger.CompoundEventTrigger,

    # Infrastructure
    "road_accessibility": road_accessibility_score.RoadAccessibilityScore,
    "grid_overload": grid_overload_trigger.GridOverloadTrigger,
    "communication_risk": communication_risk_proxy.CommunicationRiskProxy,

    # DAO
    "fallback_disbursement": disbursement_delay_fallback.DisbursementDelayFallback,
    "macro_fiscal": macro_fiscal_trigger.MacroFiscalTrigger,
    "pricing_recalibration": pricing_recalibration_engine.PricingRecalibrationEngine,
}

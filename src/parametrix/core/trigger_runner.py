import yaml
from parametrix.core.trigger_registry import TRIGGER_REGISTRY

class TriggerRunner:
    def __init__(self, config_path: str):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        self.triggers = self._initialize_triggers()

    def _initialize_triggers(self):
        triggers = []
        for trig_cfg in self.config.get("triggers", []):
            trig_type = trig_cfg["type"]
            params = trig_cfg.get("params", {})
            trig_cls = TRIGGER_REGISTRY.get(trig_type)
            if trig_cls is None:
                raise ValueError(f"Unknown trigger type: {trig_type}")
            triggers.append(trig_cls(**params))
        return triggers

    def run_all(self, inputs: dict):
        return {
            trigger.__class__.__name__: trigger.evaluate(inputs)
            for trigger in self.triggers
        }

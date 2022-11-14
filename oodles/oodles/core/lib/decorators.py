def signal_fn(func):
    def inner(inputs, outputs, extra_args={}):
        return func(inputs, outputs, extra_args=extra_args)

    return inner


def monitor(framework_obj):
    def decorator(fn):
        def wrapped(inputs):
            outputs = fn(inputs)
            framework_obj.check_for_data_drift(inputs, outputs)
            framework_obj.check_for_custom_monitor(inputs, outputs)
            framework_obj.smartly_add_data(inputs, outputs)
            if framework_obj.need_retraining():
                framework_obj.retrain()
            return outputs

        return wrapped

    return decorator

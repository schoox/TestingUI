from config import set_before_feature, set_after

def before_feature(context, feature):
    if feature.name == "UI":
        set_before_feature(context, 617024721)


def after_feature(context, feature):
    set_after(context)

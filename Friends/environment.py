from config import set_before_feature, set_after

def before_feature(context, feature):
    if feature.name == "UI":
        set_before_feature(context, 617024721)
    elif feature.name == "UI_User":
        set_before_feature(context, 617024721, user_id=2132261527)


def after_feature(context, feature):
    set_after(context)

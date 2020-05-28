from config import set_before_feature, set_after

def before_feature(context, feature):
    if feature.name == "UI":
        set_before_feature(context, 617024721)
    elif feature.name == "UI_Group":
        set_before_feature(context, 617024721, group_id=63291)


def after_feature(context, feature):
    set_after(context)

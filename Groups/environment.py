from config import set_before_feature, set_after

def before_feature(context, feature):
    set_before_feature(context, 617024721)
    context.group_id = 63291


def after_feature(context, feature):
    set_after(context)

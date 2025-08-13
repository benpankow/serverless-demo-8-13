import dagster as dg
from dagster_analytics_dependency import foo


@dg.asset(name=foo)
def foo_asset():
    pass

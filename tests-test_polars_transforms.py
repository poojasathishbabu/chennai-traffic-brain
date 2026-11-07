import polars as pl
from src_transforms_polars_transforms import clean_and_enrich, congestion_score
def test_clean():
    df=pl.DataFrame({'ts':[1,2],'speed_kmh':[30,999],'lat':[13.05,13.05],'lon':[80.24,80.24],'corridor':['OMR','OMR']})
    assert clean_and_enrich(df).height==1
def test_score(): assert 0 <= congestion_score(20,1000) <= 100

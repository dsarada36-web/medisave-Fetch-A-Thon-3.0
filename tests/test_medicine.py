from medicine import assess, find_drugs


def test_find_three_brands():
    found = {drug["brand"] for drug in find_drugs("Telma 40, Atorva 10, Pan 40")}
    assert found == {"Telma 40", "Atorva 10", "Pan 40"}


def test_savings_for_test_case():
    result = assess("Telma 40, Atorva 10, Pan 40", 1850)
    assert result.brand_total == 1850
    assert result.generic_total == 620
    assert result.monthly_saving == 1230
    assert result.annual_saving == 14760


def test_no_match_returns_zero():
    result = assess("Unknowndrug 10", 500)
    assert result.items == []
    assert result.monthly_saving == 0


def test_bill_total_overrides_dataset_sum():
    result = assess("Telma 40", 900)
    assert result.brand_total == 900
    assert result.generic_total == 240
    assert result.monthly_saving == 660


def test_same_molecule_is_deduped():
    result = assess("Pan 40 and Pantocid 40", 550)
    assert len(result.items) == 1

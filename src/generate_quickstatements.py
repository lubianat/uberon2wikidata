from wdcuration import print_quickstatements_for_curated_sheet
import pandas as pd


def main():
    curated_sheet_path = "results/curation_sheet.csv"

    df = pd.read_csv(curated_sheet_path, dtype={"id": object})

    fixed_ids = []
    for id in df["id"]:
        id = str(id)
        leading_zeros = "0" * (7 - len(id))

        new_id = leading_zeros + id
        fixed_ids.append(new_id)

    df["id"] = fixed_ids
    df.to_csv(curated_sheet_path, index=False)
    print_quickstatements_for_curated_sheet(
        curated_sheet_path, wikidata_property="P1554", dropnas=True
    )


if __name__ == "__main__":
    main()

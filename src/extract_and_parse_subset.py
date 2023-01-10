from wdcuration import generate_curation_spreadsheet


def main():
    generate_curation_spreadsheet(
        identifiers_property="P1554",
        curation_table_path="data/uberon_clean.csv",
        description_term_lookup="muscle",
        output_file_path="results/curation_sheet.csv",
        exclude_basic=True,
    )


if __name__ == "__main__":
    main()

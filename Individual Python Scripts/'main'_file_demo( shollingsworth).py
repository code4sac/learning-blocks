#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Working Demo."""
import current_grades


def main():
    """Run main function."""
    api = current_grades.Api("815", "ReportCard")
    out = api.get_current_grades_csv()
    print(out)


if __name__ == "__main__":
    main()

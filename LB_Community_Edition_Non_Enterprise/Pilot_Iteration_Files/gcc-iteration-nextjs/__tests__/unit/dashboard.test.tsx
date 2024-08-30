import { describe, expect, test } from "vitest";
import { render } from "@testing-library/react";
import Table01 from "@/app/_components/ui/table/Table01";
import mockData from "@/__tests__/mock/exampleTableData.json";

describe("General Table Tests", async () => {
  test("Mock data test: Table should contain 2 items.", () => {
    const { getByTestId } = render(<Table01 data={mockData} />);

    expect(getByTestId("table_body_01").children.length).toBe(2);
  });
});

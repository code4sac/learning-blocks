import { createColumnHelper } from "@tanstack/react-table";
import { TableStudent } from "@/app/utilities/models/table";

export function getDefaultColumns() {
  const columnHelper = createColumnHelper<TableStudent>();

  return [
    columnHelper.accessor("photo", {
      header: () => <span>Photo </span>,
      cell: (info) => <i>{info.getValue()} </i>,
    }),
    columnHelper.accessor((row) => row.studentId, {
      id: "studentId",
      header: () => <span>Student ID</span>,
    }),
    columnHelper.accessor("name", {
      header: () => "Name",
      cell: (info) => info.renderValue(),
    }),
    columnHelper.accessor("grade", {
      header: "Grade",
    }),
    columnHelper.accessor("gender", {
      header: "Gender",
    }),
    columnHelper.accessor("ethnicityCode", {
      header: "Ethnicity",
    }),
  ];
}

type Person = {
  firstName: string;
  lastName: string;
  age: number;
  visits: number;
  status: string;
  progress: number;
};

const defaultData: Person[] = [
  {
    firstName: "tanner",
    lastName: "linsley",
    age: 24,
    visits: 100,
    status: "In Relationship",
    progress: 50,
  },
  {
    firstName: "tandy",
    lastName: "miller",
    age: 40,
    visits: 40,
    status: "Single",
    progress: 80,
  },
  {
    firstName: "joe",
    lastName: "dirte",
    age: 45,
    visits: 20,
    status: "Complicated",
    progress: 10,
  },
];

import {createColumnHelper,} from '@tanstack/react-table'
import {TableStudent} from '@/utils/models/table'

export function getDefaultColumns() {
  const columnHelper = createColumnHelper<TableStudent>()

  return [
    columnHelper.accessor('photo', {
      header: () => <span>Photo </span>,
      cell: info => <i>{info.getValue()} </i>,
    }),
    columnHelper.accessor(row => row.studentId, {
      id: 'studentId',
      header: () => <span>Student ID</span>,
    }),
    columnHelper.accessor('name', {
      header: () => 'Name',
      cell: info => info.renderValue(),
    }),
    columnHelper.accessor('grade', {
      header: 'Grade',
    }),
    columnHelper.accessor('gender', {
      header: 'Gender',
    }),
    columnHelper.accessor('ethnicityCode', {
      header: 'Ethnicity',
    }),
  ]
}
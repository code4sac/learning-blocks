<script lang="tsx" setup>

import type { FunctionalComponent } from 'vue'
import { ref, unref } from 'vue'
import type { CheckboxValueType, Column } from 'element-plus'
import { ElCheckbox, ElEmpty } from 'element-plus'

type SelectionCellProps = {
  value: boolean
  intermediate?: boolean
  onChange: (value: CheckboxValueType) => void
}

const SelectionCell: FunctionalComponent<SelectionCellProps> = ({
                                                                  value,
                                                                  intermediate = false,
                                                                  onChange,
                                                                }) => {
  return (
      <ElCheckbox
          onChange={onChange}
          modelValue={value}
          indeterminate={intermediate}
      />
  )
}

const generateColumns = (length = 10, prefix = 'column-', props?: any) =>
    Array.from({length}).map((_, columnIndex) => ({
      ...props,
      key: `${prefix}${columnIndex}`,
      dataKey: `${prefix}${columnIndex}`,
      title: `Column ${columnIndex}`,
      width: 150,
    }))

const generateData = (
    columns: ReturnType<typeof generateColumns>,
    length = 200,
    prefix = 'row-'
) =>
    Array.from({length}).map((_, rowIndex) => {
      return columns.reduce(
          (rowData, column, columnIndex) => {
            rowData[column.dataKey] = `Row ${rowIndex} - Col ${columnIndex}`
            return rowData
          },
          {
            id: `${prefix}${rowIndex}`,
            checked: false,
            parentId: null,
          }
      )
    })

const columns: Column<any>[] = generateColumns(10)
columns.unshift({
  key: 'selection',
  width: 50,
  cellRenderer: ({rowData}) => {
    const onChange = (value: CheckboxValueType) => (rowData.checked = value)
    return <SelectionCell value={rowData.checked} onChange={onChange}/>
  },

  headerCellRenderer: () => {
    const _data = unref(data)
    const onChange = (value: CheckboxValueType) =>
        (data.value = _data.map((row) => {
          row.checked = value
          return row
        }))
    const allSelected = _data.every((row) => row.checked)
    const containsChecked = _data.some((row) => row.checked)

    return (
        <SelectionCell
            value={allSelected}
            intermediate={containsChecked && !allSelected}
            onChange={onChange}
        />
    )
  },
})

// const data = ref([])
const data = ref(generateData(columns, 200))

</script>

<template>
  <div style="height: 300px">
    <el-auto-resizer>
      <template #default="{ height, width }">
        <el-table-v2
            :columns="columns"
            :data=[]
            :fixed="false"
            :height="height"
            :width="width">
          <template #empty>
            <div class="flex items-center justify-center h-100%">
              <el-empty/>
            </div>
          </template>
        </el-table-v2>
      </template>
    </el-auto-resizer>
  </div>
</template>

<style scoped>

</style>
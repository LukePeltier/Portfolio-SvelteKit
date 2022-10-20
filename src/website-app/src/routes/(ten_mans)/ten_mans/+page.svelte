<script lang="ts">
  import type { PageData } from './$types';
  import { createTable, Subscribe, Render } from 'svelte-headless-table';
  import { readable } from 'svelte/store';
  export let data: PageData;

  const tableData: {
    name: string;
    top: number;
    jungle: number;
    mid: number;
    bot: number;
    support: number;
  }[] = [];

  let sortedRows = data.rows.sort(function (a, b) {
    if (a.name < b.name) return -1;
    if (a.name > b.name) return 1;
    return 0;
  });

  for (const row of sortedRows) {
    tableData.push(row);
  }

  const readableTable = readable(tableData);

  const table = createTable(readableTable);

  const columns = table.createColumns([
    table.column({
      header: 'Name',
      accessor: 'name'
    }),
    table.column({
      header: 'Top',
      accessor: 'top'
    }),
    table.column({
      header: 'Jungle',
      accessor: 'jungle'
    }),
    table.column({
      header: 'Mid',
      accessor: 'mid'
    }),
    table.column({
      header: 'Bot',
      accessor: 'bot'
    }),
    table.column({
      header: 'Support',
      accessor: 'support'
    })
  ]);

  const { headerRows, rows, tableAttrs, tableBodyAttrs } = table.createViewModel(columns);
</script>

<svelte:head>
  <title>10 Mans Statistics</title>
</svelte:head>

<div class="grid-container grid grid-cols-2 justify-items-stretch gap-4 m-12">
  <div id="playCountWrapper" class="">
    <table {...$tableAttrs}>
      <thead>
        {#each $headerRows as headerRow (headerRow.id)}
          <Subscribe rowAttrs={headerRow.attrs()} let:rowAttrs>
            <tr {...rowAttrs}>
              {#each headerRow.cells as cell (cell.id)}
                <Subscribe attrs={cell.attrs()} let:attrs>
                  <th {...attrs}>
                    <Render of={cell.render()} />
                  </th>
                </Subscribe>
              {/each}
            </tr>
          </Subscribe>
        {/each}
      </thead>
      <tbody {...$tableBodyAttrs}>
        {#each $rows as row (row.id)}
          <Subscribe rowAttrs={row.attrs()} let:rowAttrs>
            <tr {...rowAttrs}>
              {#each row.cells as cell (cell.id)}
                <Subscribe attrs={cell.attrs()} let:attrs>
                  <td {...attrs}>
                    <Render of={cell.render()} />
                  </td>
                </Subscribe>
              {/each}
            </tr>
          </Subscribe>
        {/each}
      </tbody>
    </table>
  </div>
  <div id="winPercentWrapper" class="">
    <table {...$tableAttrs}>
      <thead>
        {#each $headerRows as headerRow (headerRow.id)}
          <Subscribe rowAttrs={headerRow.attrs()} let:rowAttrs>
            <tr {...rowAttrs}>
              {#each headerRow.cells as cell (cell.id)}
                <Subscribe attrs={cell.attrs()} let:attrs>
                  <th {...attrs}>
                    <Render of={cell.render()} />
                  </th>
                </Subscribe>
              {/each}
            </tr>
          </Subscribe>
        {/each}
      </thead>
      <tbody {...$tableBodyAttrs}>
        {#each $rows as row (row.id)}
          <Subscribe rowAttrs={row.attrs()} let:rowAttrs>
            <tr {...rowAttrs}>
              {#each row.cells as cell (cell.id)}
                <Subscribe attrs={cell.attrs()} let:attrs>
                  <td {...attrs}>
                    <Render of={cell.render()} />
                  </td>
                </Subscribe>
              {/each}
            </tr>
          </Subscribe>
        {/each}
      </tbody>
    </table>
  </div>
</div>

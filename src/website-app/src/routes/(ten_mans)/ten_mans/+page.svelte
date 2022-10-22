<script lang="ts">
  import type { PageData } from './$types';
  import { createTable, Subscribe, Render } from 'svelte-headless-table';
  import { readable } from 'svelte/store';
  export let data: PageData;

  const gamesPlayedTableData: {
    name: string;
    top: number;
    jungle: number;
    mid: number;
    bot: number;
    support: number;
  }[] = [];

  let gamesPlayedSortedRows = data.gamesPlayed.sort(function (a, b) {
    if (a.name < b.name) return -1;
    if (a.name > b.name) return 1;
    return 0;
  });

  for (const row of gamesPlayedSortedRows) {
    gamesPlayedTableData.push(row);
  }

  const gamesPlayedReadableTable = readable(gamesPlayedTableData);

  const gamesPlayedTable = createTable(gamesPlayedReadableTable);

  const gamesPlayedColumns = gamesPlayedTable.createColumns([
    gamesPlayedTable.column({
      header: 'Name',
      accessor: 'name'
    }),
    gamesPlayedTable.column({
      header: 'Top',
      accessor: 'top'
    }),
    gamesPlayedTable.column({
      header: 'Jungle',
      accessor: 'jungle'
    }),
    gamesPlayedTable.column({
      header: 'Mid',
      accessor: 'mid'
    }),
    gamesPlayedTable.column({
      header: 'Bot',
      accessor: 'bot'
    }),
    gamesPlayedTable.column({
      header: 'Support',
      accessor: 'support'
    })
  ]);

  const {
    headerRows: gamesPlayed_headerRows,
    rows: gamesPlayed_rows,
    tableAttrs: gamesPlayed_tableAttrs,
    tableBodyAttrs: gamesPlayed_tableBodyAttrs
  } = gamesPlayedTable.createViewModel(gamesPlayedColumns);

  const gamesWonTableData: {
    name: string;
    top: string;
    jungle: string;
    mid: string;
    bot: string;
    support: string;
  }[] = [];

  let gamesWonSortedRows = data.gamesWon.sort(function (a, b) {
    if (a.name < b.name) return -1;
    if (a.name > b.name) return 1;
    return 0;
  });

  for (const row of gamesWonSortedRows) {
    gamesWonTableData.push(row);
  }

  const gamesWonReadableTable = readable(gamesWonTableData);

  const gamesWonTable = createTable(gamesWonReadableTable);

  const gamesWonColumns = gamesWonTable.createColumns([
    gamesWonTable.column({
      header: 'Name',
      accessor: 'name'
    }),
    gamesWonTable.column({
      header: 'Top',
      accessor: 'top'
    }),
    gamesWonTable.column({
      header: 'Jungle',
      accessor: 'jungle'
    }),
    gamesWonTable.column({
      header: 'Mid',
      accessor: 'mid'
    }),
    gamesWonTable.column({
      header: 'Bot',
      accessor: 'bot'
    }),
    gamesWonTable.column({
      header: 'Support',
      accessor: 'support'
    })
  ]);

  const {
    headerRows: gamesWon_headerRows,
    rows: gamesWon_rows,
    tableAttrs: gamesWon_tableAttrs,
    tableBodyAttrs: gamesWon_tableBodyAttrs
  } = gamesWonTable.createViewModel(gamesWonColumns);
</script>

<svelte:head>
  <title>10 Mans Statistics</title>
</svelte:head>

<div class="grid-container grid grid-cols-2 justify-items-stretch gap-4 m-12">
  <div id="winPercentWrapper" class="">
    <table {...$gamesWon_tableAttrs} class="w-full text-left text-gray-500 dark:text-gray-400">
      <thead>
        {#each $gamesWon_headerRows as headerRow (headerRow.id)}
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
      <tbody {...$gamesWon_tableBodyAttrs}>
        {#each $gamesWon_rows as row (row.id)}
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
  <div id="playCountWrapper" class="">
    <table {...$gamesPlayed_tableAttrs} class="w-full text-left text-gray-500 dark:text-gray-400">
      <thead class="text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
        {#each $gamesPlayed_headerRows as headerRow (headerRow.id)}
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
      <tbody {...$gamesPlayed_tableBodyAttrs}>
        {#each $gamesPlayed_rows as row (row.id)}
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

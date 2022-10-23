<script lang="ts">
  import type { PageData } from './$types';
  import { createTable, Subscribe, Render } from 'svelte-headless-table';
  import { addSortBy } from 'svelte-headless-table/plugins';
  import { readable } from 'svelte/store';
  export let data: PageData;

  function getStatSortValue(i: string): number {
    if (i === 'N/A') {
      return -1;
    }

    if (i.includes('%')) {
      const num_string = i.replaceAll('%', '');
      return Number(num_string);
    } else {
      console.error('Error, received string which cannot be sorted', i);
      return -2;
    }
  }

  /**
   * Games Played Table
   */
  const gamesPlayedReadableTable = readable(data.gamesPlayed);

  const gamesPlayedTable = createTable(gamesPlayedReadableTable, {
    sort: addSortBy({ initialSortKeys: [{ id: 'name', order: 'asc' }] })
  });

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

  /**
   * Games Won Table
   */

  const gamesWonReadableTable = readable(data.gamesWon);

  const gamesWonTable = createTable(gamesWonReadableTable, {
    sort: addSortBy({ initialSortKeys: [{ id: 'name', order: 'asc' }], disableMultiSort: true })
  });

  const gamesWonColumns = gamesWonTable.createColumns([
    gamesWonTable.column({
      header: 'Name',
      accessor: 'name'
    }),
    gamesWonTable.column({
      header: 'Top',
      accessor: 'top',
      plugins: {
        sort: {
          getSortValue: (i) => getStatSortValue(i)
        }
      }
    }),
    gamesWonTable.column({
      header: 'Jungle',
      accessor: 'jungle',
      plugins: {
        sort: {
          getSortValue: (i) => getStatSortValue(i)
        }
      }
    }),
    gamesWonTable.column({
      header: 'Mid',
      accessor: 'mid',
      plugins: {
        sort: {
          getSortValue: (i) => getStatSortValue(i)
        }
      }
    }),
    gamesWonTable.column({
      header: 'Bot',
      accessor: 'bot',
      plugins: {
        sort: {
          getSortValue: (i) => getStatSortValue(i)
        }
      }
    }),
    gamesWonTable.column({
      header: 'Support',
      accessor: 'support',
      plugins: {
        sort: {
          getSortValue: (i) => getStatSortValue(i)
        }
      }
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

<div class="m-12 grid grid-cols-2 justify-items-stretch gap-4 ">
  <div id="winPercentWrapper" class="">
    <table
      {...$gamesWon_tableAttrs}
      class="table w-full text-left text-gray-500 dark:text-gray-400"
    >
      <thead>
        {#each $gamesWon_headerRows as headerRow (headerRow.id)}
          <Subscribe rowAttrs={headerRow.attrs()} let:rowAttrs>
            <tr {...rowAttrs}>
              {#each headerRow.cells as cell (cell.id)}
                <Subscribe attrs={cell.attrs()} let:attrs props={cell.props()} let:props>
                  <th {...attrs} on:click={props.sort.toggle}>
                    <Render of={cell.render()} />
                    {#if props.sort.order === 'asc'}
                      ⬇️
                    {:else if props.sort.order === 'desc'}
                      ⬆️
                    {/if}
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
            <tr {...rowAttrs} class="hover">
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
    <table
      {...$gamesPlayed_tableAttrs}
      class="table w-full text-left text-gray-500 dark:text-gray-400"
    >
      <thead class="">
        {#each $gamesPlayed_headerRows as headerRow (headerRow.id)}
          <Subscribe rowAttrs={headerRow.attrs()} let:rowAttrs>
            <tr {...rowAttrs}>
              {#each headerRow.cells as cell (cell.id)}
                <Subscribe attrs={cell.attrs()} let:attrs props={cell.props()} let:props>
                  <th {...attrs} on:click={props.sort.toggle}>
                    <Render of={cell.render()} />
                    {#if props.sort.order === 'asc'}
                      ⬇️
                    {:else if props.sort.order === 'desc'}
                      ⬆️
                    {/if}
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
            <tr {...rowAttrs} class="hover">
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

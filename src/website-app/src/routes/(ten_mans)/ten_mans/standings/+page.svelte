<script lang="ts">
  import type { PageData } from './$types';
  import type { PlayerGamesWon, PlayerGamesPlayed } from './proxy+page.server';
  import type { ColumnDef, TableOptions, SortingState } from '@tanstack/svelte-table';
  import {
    createSvelteTable,
    flexRender,
    getCoreRowModel,
    getSortedRowModel
  } from '@tanstack/svelte-table';
  import { writable } from 'svelte/store';
  // import Grid from 'gridjs-svelte';
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

  function compareStats(a: string, b: string): number {
    let aSortValue = getStatSortValue(a);
    let bSortValue = getStatSortValue(b);
    if (aSortValue > bSortValue) {
      return 1;
    } else if (bSortValue > aSortValue) {
      return -1;
    }
    return 0;
  }

  const gamesWonColumns: ColumnDef<PlayerGamesWon>[] = [
    {
      accessorKey: 'name',
      header: 'Name'
    },
    {
      accessorKey: 'top',
      header: 'Top'
    },
    {
      accessorKey: 'jungle',
      header: 'Jungle'
    },
    {
      accessorKey: 'mid',
      header: 'Middle'
    },
    {
      accessorKey: 'bot',
      header: 'Bottom'
    },
    {
      accessorKey: 'support',
      header: 'Support'
    },
    {
      accessorKey: 'total',
      header: 'Overall'
    }
  ];

  let gamesWonSorting: SortingState = [];

  const setGamesWonSorting = (updater: SortingState | ((arg0: SortingState) => SortingState)) => {
    if (updater instanceof Function) {
      gamesWonSorting = updater(gamesWonSorting);
    } else {
      gamesWonSorting = updater;
    }

    gamesWonOptions.update((old) => ({
      ...old,
      state: {
        ...old.state,
        gamesWonSorting
      }
    }));
  };

  const gamesWonOptions = writable<TableOptions<PlayerGamesWon>>({
    data: data.gamesWon,
    columns: gamesWonColumns,
    state: {
      gamesWonSorting
    },
    onSortingChange: setGamesWonSorting,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel()
  });

  const gamesWonTable = createSvelteTable(gamesWonOptions);

  const gamesPlayedColumns: ColumnDef<PlayerGamesPlayed>[] = [
    {
      accessorKey: 'name',
      header: 'Name'
    },
    {
      accessorKey: 'top',
      header: 'Top'
    },
    {
      accessorKey: 'jungle',
      header: 'Jungle'
    },
    {
      accessorKey: 'mid',
      header: 'Middle'
    },
    {
      accessorKey: 'bot',
      header: 'Bottom'
    },
    {
      accessorKey: 'support',
      header: 'Support'
    },
    {
      accessorKey: 'total',
      header: 'Overall'
    }
  ];

  const gamesPlayedOptions = writable<TableOptions<PlayerGamesPlayed>>({
    data: data.gamesPlayed,
    columns: gamesPlayedColumns,
    getCoreRowModel: getCoreRowModel()
  });

  const gamesPlayedTable = createSvelteTable(gamesPlayedOptions);
</script>

<svelte:head>
  <title>10 Mans Statistics Standings</title>
</svelte:head>

<div class="m-12 flex flex-row justify-items-stretch gap-4">
  <div>
    <table>
      <thead>
        {#each $gamesWonTable.getHeaderGroups() as headerGroup}
          <tr>
            {#each headerGroup.headers as header}
              <th>
                {#if !header.isPlaceholder}
                  <svelte:component
                    this={flexRender(header.column.columnDef.header, header.getContext())}
                  />
                {/if}
              </th>
            {/each}
          </tr>
        {/each}
      </thead>
      <tbody>
        {#each $gamesWonTable.getRowModel().rows as row}
          <tr>
            {#each row.getVisibleCells() as cell}
              <td>
                <svelte:component
                  this={flexRender(cell.column.columnDef.cell, cell.getContext())}
                />
              </td>
            {/each}
          </tr>
        {/each}
      </tbody>
      <tfoot />
    </table>
  </div>
  <div>
    <table>
      <thead>
        {#each $gamesPlayedTable.getHeaderGroups() as headerGroup}
          <tr>
            {#each headerGroup.headers as header}
              <th>
                {#if !header.isPlaceholder}
                  <svelte:component
                    this={flexRender(header.column.columnDef.header, header.getContext())}
                  />
                {/if}
              </th>
            {/each}
          </tr>
        {/each}
      </thead>
      <tbody>
        {#each $gamesPlayedTable.getRowModel().rows as row}
          <tr>
            {#each row.getVisibleCells() as cell}
              <td>
                <svelte:component
                  this={flexRender(cell.column.columnDef.cell, cell.getContext())}
                />
              </td>
            {/each}
          </tr>
        {/each}
      </tbody>
      <tfoot />
    </table>
  </div>
</div>

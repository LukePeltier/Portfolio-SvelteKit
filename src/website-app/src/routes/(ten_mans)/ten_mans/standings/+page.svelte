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
  import Fa from 'svelte-fa';
  import { faSort, faSortUp, faSortDown } from '@fortawesome/free-solid-svg-icons';
  export let data: PageData;

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

  let gamesWonSorting: SortingState = [
    {
      id: 'name',
      desc: false
    }
  ];

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
        sorting: gamesWonSorting
      }
    }));
  };

  const gamesWonOptions = writable<TableOptions<PlayerGamesWon>>({
    data: data.gamesWon,
    columns: gamesWonColumns,
    state: {
      sorting: gamesWonSorting
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

  let gamesPlayedSorting: SortingState = [
    {
      id: 'name',
      desc: false
    }
  ];

  const setgamesPlayedSorting = (
    updater: SortingState | ((arg0: SortingState) => SortingState)
  ) => {
    if (updater instanceof Function) {
      gamesPlayedSorting = updater(gamesPlayedSorting);
    } else {
      gamesPlayedSorting = updater;
    }

    gamesPlayedOptions.update((old) => ({
      ...old,
      state: {
        ...old.state,
        sorting: gamesPlayedSorting
      }
    }));
  };

  const gamesPlayedOptions = writable<TableOptions<PlayerGamesPlayed>>({
    data: data.gamesPlayed,
    columns: gamesPlayedColumns,
    state: {
      sorting: gamesPlayedSorting
    },
    onSortingChange: setgamesPlayedSorting,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel()
  });

  const gamesPlayedTable = createSvelteTable(gamesPlayedOptions);
</script>

<svelte:head>
  <title>10 Mans Statistics Standings</title>
</svelte:head>

<div class="m-12 grid grid-cols-2 justify-items-center gap-4">
  <div>
    <table class="table">
      <thead>
        {#each $gamesWonTable.getHeaderGroups() as headerGroup}
          <tr>
            {#each headerGroup.headers as header}
              <th>
                {#if !header.isPlaceholder}
                  <!-- svelte-ignore a11y-click-events-have-key-events -->
                  <div
                    class:cursor-pointer={header.column.getCanSort()}
                    class:select-none={header.column.getCanSort()}
                    on:click={header.column.getToggleSortingHandler()}
                  >
                    <svelte:component
                      this={flexRender(header.column.columnDef.header, header.getContext())}
                    />
                    {#if header.column.getIsSorted().toString() == 'asc'}
                      <Fa icon={faSortUp} class="inline" />
                    {:else if header.column.getIsSorted().toString() == 'desc'}
                      <Fa icon={faSortDown} class="inline" />
                    {:else}
                      <Fa icon={faSort} class="inline" />
                    {/if}
                  </div>
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
    <table class="table">
      <thead>
        {#each $gamesPlayedTable.getHeaderGroups() as headerGroup}
          <tr>
            {#each headerGroup.headers as header}
              <th>
                {#if !header.isPlaceholder}
                  <!-- svelte-ignore a11y-click-events-have-key-events -->
                  <div
                    class:cursor-pointer={header.column.getCanSort()}
                    class:select-none={header.column.getCanSort()}
                    on:click={header.column.getToggleSortingHandler()}
                  >
                    <svelte:component
                      this={flexRender(header.column.columnDef.header, header.getContext())}
                    />
                    {#if header.column.getIsSorted().toString() == 'asc'}
                      <Fa icon={faSortUp} class="inline" />
                    {:else if header.column.getIsSorted().toString() == 'desc'}
                      <Fa icon={faSortDown} class="inline" />
                    {:else}
                      <Fa icon={faSort} class="inline" />
                    {/if}
                  </div>
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

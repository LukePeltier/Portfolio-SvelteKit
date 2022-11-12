<script lang="ts">
  import type { PageData } from './$types';
  import Grid from 'gridjs-svelte';
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
   * Games Won Table
   */

  const gamesWonData = data.gamesWon;
  const gamesWonColumns = [
    {
      name: 'Name'
    }
  ];

  /**
   * Games Played Table
   */
  const gamesPlayedReadableTable = data.gamesPlayed;
</script>

<svelte:head>
  <title>10 Mans Statistics</title>
</svelte:head>

<div class="m-12 grid grid-cols-2 justify-items-stretch gap-4 ">
  <Grid data={gamesWonData} sort />
  <!-- <div id="playCountWrapper" class="">
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
  </div> -->
</div>

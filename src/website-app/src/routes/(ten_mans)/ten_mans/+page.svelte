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

  /**
   * Games Won Table
   */
  const gamesWonData = data.gamesWon;

  /**
   * Games Played Table
   */
  const gamesPlayedData = data.gamesPlayed;

  const gameTablesClasses = {
    table: "w-full"
  };
  const gamesColumns = [
    {
      name: 'Name'
    },
    {
      name: 'Top',
      sort: {
        compare: compareStats
      }
    },
    {
      name: 'Jungle',
      sort: {
        compare: compareStats
      }
    },
    {
      name: 'Mid',
      sort: {
        compare: compareStats
      }
    },
    {
      name: 'Bot',
      sort: {
        compare: compareStats
      }
    },
    {
      name: 'Support',
      sort: {
        compare: compareStats
      }
    }
  ];
</script>

<svelte:head>
  <title>10 Mans Statistics</title>
</svelte:head>

<div class="m-12 flex flex-row justify-items-stretch gap-4 ">
  <div>
    <Grid data={gamesWonData} sort columns={gamesColumns} className={gameTablesClasses} />
  </div>
  <div>
    <Grid data={gamesPlayedData} sort columns={gamesColumns} className={gameTablesClasses} />
  </div>
</div>

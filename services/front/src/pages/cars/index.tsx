import * as React from 'react';
import { RowsProp, DataGrid, PageChangeParams } from '@material-ui/data-grid';
import { Cars, Car } from '../../types'
import Layout from '../../components/Layout'
import AddIcon from '@material-ui/icons/Add';
import Fab from '@material-ui/core/Fab';
import { makeStyles, useTheme, Theme, createStyles } from '@material-ui/core/styles';
import { useRouter } from 'next/router';


const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    fab: {
      position: 'fixed',
      bottom: '12%',
      right: '15%',      
    },
  }),
);

const loadServerRows = async (page: number) => {
    const res = await fetch(`/api/cars?page=${page}`)
    return res.json()
}

export default function CarsList() {
  const [page, setPage] = React.useState(0);
  const [rows, setRows] = React.useState<RowsProp>([]);
  const [rowsAmount, setRowsAmount] = React.useState<number>(0);
  const [loading, setLoading] = React.useState<boolean>(false);
  const router = useRouter();
  const classes = useStyles();

  const columns = [
    { field: 'id', label: 'UUID', width: 230 },
    { field: 'make', label: 'MAKE', width: 130 },
    { field: 'model', label: 'MODEL', width: 130 },
    { field: 'year', label: 'YEAR', width: 100 },
  ];

  const handlePageChange = (params: PageChangeParams) => {
    setPage(params.page);
  };

  React.useEffect(() => {
    let active = true;

    (async () => {
      setLoading(true);
       const data: Cars = await loadServerRows(page);
       const newRows: Car[] = data.cars;

      if (!active) {
        return;
      }

      setRowsAmount(data.amount);
      setRows(newRows);
      setLoading(false);
    })();

    return () => {
      active = false;
    };
  }, [page]);

  return (
    <Layout>
        <div style={{height:"500px"}}>
            <DataGrid
                rows={rows}
                columns={columns}
                pagination
                pageSize={50}
                rowCount={rowsAmount}
                paginationMode="server"
                onPageChange={handlePageChange}
                loading={loading}
            />
        </div>

        <Fab
            color="primary"
            className={classes.fab}
            aria-label="add"
            onClick={() => router.push(`${router.pathname}/add`)}>   
                <AddIcon />
        </Fab>

    </Layout>
  );
}
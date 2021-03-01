import React, { useState } from 'react'
import { RowsProp, DataGrid, PageChangeParams } from '@material-ui/data-grid';
import { Cars, Car } from '../../types'
import Layout from '../../components/Layout'
import clsx from 'clsx';
import { makeStyles, useTheme, Theme, createStyles } from '@material-ui/core/styles';
import { useRouter } from 'next/router';
import TextField from '@material-ui/core/TextField';
import { DatePicker, MuiPickersUtilsProvider } from '@material-ui/pickers';
import DateFnsUtils from "@date-io/date-fns";
import Button from '@material-ui/core/Button';
import CircularProgress from '@material-ui/core/CircularProgress';
import { green } from '@material-ui/core/colors';
import { Alert, AlertTitle } from '@material-ui/lab';
import Collapse from '@material-ui/core/Collapse';
import IconButton from '@material-ui/core/IconButton';
import CloseIcon from '@material-ui/icons/Close';


const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      '& > *': {
        margin: theme.spacing(1),
      }
    },
     block: {
       display: 'block',
     },
     savebutton: {
       margin: '40px',
     },
     wrapper: {
      margin: theme.spacing(1),
      position: 'relative',
    },
    buttonSuccess: {
      backgroundColor: green[500],
      '&:hover': {
        backgroundColor: green[700],
      },
    },
    buttonProgress: {
      color: green[500],
      position: 'absolute',
      top: '50%',
      left: '50%',
      marginTop: -12,
      marginLeft: -12,
    }
  }),
);


interface FormStatus {
  helperText: string
  error: boolean
}


const AddCarPage = () => {  
  const [loading, setLoading] = React.useState<boolean>(false);
  const router = useRouter();
  const classes = useStyles();
  const [selectedDate, handleDateChange] = useState(new Date());
  const [stateField, setStateField] = useState<FormStatus>({ helperText: '', error: false });
  const [success, setSuccess] = React.useState(false);
  const [collapse, setCollapse] = React.useState(false);

  const buttonClassname = clsx({
    [classes.buttonSuccess]: success,
  });

  const onChangeField = ()=>{
    setStateField({ helperText: '', error: false });
  }

  const onCheckField = (fields: string[]) => {
    for(let field of fields){
      if(field.length > 128 || field.length < 2){
        setStateField({ helperText: 'correct text 1 < len < 128 ', error: true });
        return false;
      }
    }
    return true;
  }

  const submitData = async (event) => {
    event.preventDefault()

    let make = event.target.elements.make.value;
    let model = event.target.elements.model.value;

    if(!onCheckField([make, model])){
      return;
    }

    try {
      let data: Car = { make: event.target.elements.make.value, 
                        model: event.target.elements.model.value, 
                        year: new DateFnsUtils().getYear(selectedDate).toString()
                       }
      setLoading(true);
      const res = await fetch(`/api/cars`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      })

      if (res.status != 200){
        setCollapse(true)
      }else{
        setSuccess(true);
        router.push("/")
      }
    } catch (error) {
      console.error(error)
    }finally{
      setLoading(false);
    }
  }

  
  return (
    <Layout>
      <div style={{height:"500px"}}>
        <form className={classes.root}  onSubmit={submitData}>
          <TextField required label="Make" onChange={onChangeField} name="make" error={stateField.error} helperText={stateField.helperText} />
          <TextField required label="Model" onChange={onChangeField} name="model" error={stateField.error} helperText={stateField.helperText} />
          <div className={classes.block}>
            <MuiPickersUtilsProvider utils={DateFnsUtils} >
              <DatePicker value={selectedDate} onChange={handleDateChange} views={['year']}/>
            </MuiPickersUtilsProvider>
          </div>
          <div className={classes.wrapper}>
            <Button
              variant="contained"
              color="primary"
              className={buttonClassname}
              type="submit"
              disabled={loading}
            >
              Add new cars
            </Button>
            {loading && <CircularProgress size={70} className={classes.buttonProgress} />}
          </div>          
        </form>
        <Collapse in={collapse}>
          <Alert severity="error" action={
            <IconButton
              aria-label="close"
              color="inherit"
              size="small"
              onClick={() => {
                setCollapse(false);
              }}
            >
              <CloseIcon fontSize="inherit" />
            </IconButton>
          }>
            <AlertTitle>Error</AlertTitle>
              Oooops!something went wrong!
          </Alert>
        </Collapse>
      </div>
    </Layout>
  );
}


export default AddCarPage;

export type Car = {
    uuid?: string;
    make: string;
    model: string;
    year: string;
  };
  
  export type Cars = {
      cars: Car[];
      amount: number;
  } 
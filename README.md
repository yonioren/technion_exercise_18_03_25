# Budget Manager

## Intruduction

Hi! I am Yoni and I am a student at the Technion's DevOps Professional Course.
This is schoolwork!

The system will add a log of incomes and expenses.

### Data source format

```
budget_data = {
    "balance": 300,
    "transactions": {
        "income": [(1000, "Salary), (500, "Rent")],
        "expense": [(200, "Drugs"), (300, "Sex"), (4000, "Rock n' Roll")]
    }
}
```

### Modules

#### Add income
* Allow multiple incomes to be added
* Calculate the balance

#### Add expense
* Allow multiple expenses to be added
* Calculate the balance

#### Show the balance

#### Show transaction log

## Web version

Using WSGI this branch is able to bring you a Web version of the system.

### Deployment steps

1. Please Directory.conf in your APACHE site-available path
2. create /var/www/py and place the rest of the files there
3. Change ownership and permissions to www-data:www-date 775.
4. a2enmod wsgi
5. apache2ctl restart
6. open a browser and enjoy


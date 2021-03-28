import React from 'react';
import { css } from 'aphrodite';
import { ApolloProvider, gql, useQuery } from '@apollo/client';

import Text from './lib/Text';
import customStyleSheet from './lib/customStyleSheet';
import evergreenIcon from './img/evergreen_icon.png';
import getImageUri from './utils/getImageUri';
import ReactTable from 'react-table-6';
import 'react-table-6/react-table.css';

const allVendors = gql`
query
{
  allVendors
  {
    name,
    description,
    externalLink,
    category,
    status,
    tier,
    risk
  }
}`;


const columns = [

  {
    Header: 'Name',
    accessor: 'name',
    sortable: true,
    filterable: true,
    width: 175
  },
  {
    Header: 'Description',
    accessor: 'description',
    sortable: true,
    filterable: true,
    width: 450
  },
  {
    Header: 'External Link',
    accessor: 'externalLink',
    sortable: true,
    filterable: true,
    width: 250
  },
  {
    Header: 'Category',
    accessor: 'category',
    sortable: true,
    filterable: true
  },
  {
    Header: 'Status',
    accessor: 'status',
    sortable: true,
    filterable: true
  },
  {
    Header: 'Tier',
    accessor: 'tier',
    sortable: true,
    filterable: true
  },
  {
    Header: 'Risk',
    accessor: 'risk',
    sortable: true,
    filterable: true
  }
];


function VendorListWithData() {
  const {loading, error, data} = useQuery(allVendors);
  if (loading) return <p>Loading...</p>
  if (error) return <p>Error...</p>
  console.log(data);
  return (
      <ReactTable className="-striped -highlight"
      data={data["allVendors"]}
      columns={columns}
      defaultPageSize={10}
      />
  )
}

const styles = customStyleSheet(({ color, bp }) => ({
  logo: {
    height: 40,
    width: 40,
    marginRight: 2 * bp,
  },
  container: {
    backgroundColor: color.background,
    height: 'flex',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    
  },
}));

function App() {
  return (
    <div className={css(styles.container)}>
      <VendorListWithData/>
    </div>
  );
}

export default App;

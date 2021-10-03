import React, { Component } from "react";
import { useTable } from "react-table";
import { useState, useMemo } from "react";

export default function Table({ columns, data }) {
  // Use the useTable Hook to send the columns and data to build the table
  const {
    getTableProps, // table props from react-table
    getTableBodyProps, // table body props from react-table
    headerGroups, // headerGroups, if your table has groupings
    rows, // rows for the table based on the data passed
    prepareRow // Prepare the row (this function needs to be called for each row before getting the row props)
  } = useTable({
    columns,
    data
  });

  /* 
      Render the UI for your table
      - react-table doesn't have UI, it's headless. We just need to put the react-table props from the Hooks, and it will do its magic automatically
    */
  return (
    <table {...getTableProps()}>
      <thead>
        {headerGroups.map(headerGroup => (
          <tr {...headerGroup.getHeaderGroupProps()}>
            {headerGroup.headers.map(column => (
              <th {...column.getHeaderProps()}>{column.render("Header")}</th>
            ))}
          </tr>
        ))}
      </thead>
      <tbody {...getTableBodyProps()}>
        {rows.map((row, i) => {
          prepareRow(row);
          return (
            <tr {...row.getRowProps()}>
              {row.cells.map(cell => {
                return <td {...cell.getCellProps()}>{cell.render("Cell")}</td>;
              })}
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}

export class LogPage extends Component {
  render() {
    const data = [
      {
        score: 17.592657,
        show: {
          id: 44813,
          url: "http://www.tvmaze.com/shows/44813/the-snow-spider",
          name: "The Snow Spider",
          type: "Scripted",
          language: "English",
          genres: ["Drama", "Fantasy"],
          status: "In Development",
          runtime: 30,
          premiered: null,
          officialSite: null,
          schedule: {
            time: "",
            days: []
          }
        }
      }
    ];

    const columns = [
        {
          // first group - TV Show
          Header: "TV Show",
          // First group columns
          columns: [
            {
              Header: "Name",
              accessor: "show.name"
            },
            {
              Header: "Type",
              accessor: "show.type"
            }
          ]
        },
        {
          // Second group - Details
          Header: "Details",
          // Second group columns
          columns: [
            {
              Header: "Language",
              accessor: "show.language"
            },
            {
              Header: "Genre(s)",
              accessor: "show.genres"
            },
            {
              Header: "Runtime",
              accessor: "show.runtime"
            },
            {
              Header: "Status",
              accessor: "show.status"
            }
          ]
        }
      ];
    return <Table columns={columns} data={data} />;
  }
}
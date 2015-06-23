var LawProjects = React.createClass({
  getInitialState: function() {
    return {
      projects: [],
      total_pages: 1,
      current_page: 1,
      items_per_page: 15,
      show_only_selected: false
    }
  },

  componentDidMount: function() {
    $.get(this.props.data_url, function(result) {
      total_pages = Math.round((result.items.length / this.state.items_per_page)+0.5);

      if (this.isMounted()) {
        this.setState({
          projects: result.items,
          total_pages: total_pages
        })
      }
    }.bind(this))
  },

  onChangePage: function(page) {
    this.setState({current_page: page});
    $.scrollTo('.law-projects', 100, {offset: -40});
  },

  showPassedOnly: function() {
    this.setState({
      show_only_selected: !this.state.show_only_selected
    });
  },

  render: function() {
    var columns = {
      number: {
        title: 'Projekto numeris',
        func: function (item) {
          return <a href={item['url']} target='_blank'>{item['number']}</a>
        }
      },
      title: {title: 'Pavadinimas', func: null},
      date: {title: 'Teikimo data', func: null},
      proposer_count: {title: 'Viso teikėjų', func: null},
      date_passed: {
        title: 'Priėmimas',
        func: function (item) {
          return (item['date_passed']) ? 'Priimtas '+item['date_passed'] : 'Nepriimtas'
        }
      },
    }

    var slice_from = (this.state.current_page-1)*this.state.items_per_page,
        slice_to = this.state.current_page*this.state.items_per_page;

    var projects = this.state.projects;
    if (this.state.show_only_selected) {
      projects = projects.filter(function(item) {
        return item.date_passed
      }.bind(this))
    }

    return (
      <div className="law-projects">
        <div className="ui page grid">
          <div className="eight wide column">
            <h2 className="title">Įstatymų projektai</h2>
          </div>
          <div className="eight wide right aligned column">
            <div className="ui toggle checkbox" onClick={this.showPassedOnly}>
              <input name="filter_passed" type="checkbox" checked={this.state.show_only_selected}/>
              <label>Rodyti tik priimtus projektus</label>
            </div>
          </div>

          <div className="ui zero margin grid">
            <SemanticTable columns={columns}
                           items={projects.slice(slice_from, slice_to)} />
          </div>
          <div className="ui center aligned grid">
            <Paginator max={this.state.total_pages} onChange={this.onChangePage} />
          </div>
        </div>
      </div>
    )
  }
});

var SemanticTable = React.createClass({
  render: function() {
    var columns = this.props.columns;
    return (
      <table className="ui zero paddings table">
        <thead>
          <tr>
            {Object.keys(columns).map(function (key) {
              return <th>{columns[key].title}</th>
            })}
          </tr>
        </thead>
        <tbody>
            {this.props.items.map(function (item) {
              return (
                <tr>
                  {Object.keys(columns).map(function (key) {
                    return (
                      <td>
                      {(columns[key].func) ? columns[key].func(item) : item[key]}
                      </td>
                    )
                  })}
                </tr>
              )
            })}
        </tbody>
      </table>
    )
  }
});


var data_url = '/json/law_projects/' + $('#law-projects-component').attr("data-slug");

React.render(
  <LawProjects data_url={data_url} />,
  document.getElementById('law-projects-component')
);

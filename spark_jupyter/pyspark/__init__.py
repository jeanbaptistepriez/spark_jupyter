# ****************************************************************************
#      Copyright (C) 2016 Jean-Baptiste Priez
#
# Distributed  under  the  terms  of  the  GNU  General  Public  License (GPL)
#                         http://www.gnu.org/licenses/
# ****************************************************************************
from pyspark.sql import DataFrame
from jinja2 import Template

class DataFrameShow:

    def __init__(self, dataframe, n, truncate):
        self._df = dataframe
        self._n = n
        self._truncate = truncate # TODO use it!

    def __repr__(self):
        return self._df._jdf.showString(self._n, self._truncate)

    def _repr_html_(self):
        header = map(lambda field: field.name, self._df.schema.fields)

        rows = [
            [row[h]             if isinstance(row[h], (str, unicode)) else
            (row[h].isoformat() if hasattr(row[h], 'isoformat') else
            (''                 if row[h] == None else
             repr(row[h])))
             for h in header]
            for row in self._df.limit(self._n).collect()
        ]
        template = Template(self._template_show)
        return template.render(header=header, rows=rows)

    _template_show = """
    <script src='http://johnny.github.io/jquery-sortable/js/jquery-sortable.js'></script>
    <table class='table table-striped table-bordered'>
        <thead class='sorted_head'>
        <tr>
        {% for cell in header %}
            <th>{{ cell }}</th>
        {% endfor %}
        </tr>
        </thead>
        <tbody>
        {% for row in rows %}
        <tr>
          {% for cell in row %}
            <td align="right"> {{ cell }} </td>
          {% endfor %}
        </tr>
        {% endfor %}
        </tbody>
    </table>
    <script>
var oldIndex;
$('.sorted_head tr').sortable({
  containerSelector: 'tr',
  itemSelector: 'th',
  placeholder: '<th class="placeholder"/>',
  vertical: false,
  onDragStart: function ($item, container, _super) {
    oldIndex = $item.index();
    $item.appendTo($item.parent());
    _super($item, container);
  },
  onDrop: function  ($item, container, _super) {
    var field,
        newIndex = $item.index();

    if(newIndex != oldIndex) {
      $item.closest('table').find('tbody tr').each(function (i, row) {
        row = $(row);
        if(newIndex < oldIndex) {
          row.children().eq(newIndex).before(row.children()[oldIndex]);
        } else if (newIndex > oldIndex) {
          row.children().eq(newIndex).after(row.children()[oldIndex]);
        }
      });
    }

    _super($item, container);
  }
});
    </script>
    """

def show(self, n=20, truncate=True):
    return DataFrameShow(self, n, truncate)

DataFrame.show = show


class DataFrameSchema:

    def __init__(self, dataframe, order):
        self._df = dataframe
        self._order = order

        self._order_action = {
            'schm': lambda : self._df.schema.fields,
            'type': lambda : sorted(self._df.schema.fields, key=lambda field: field.dataType),
            'alph': lambda : sorted(self._df.schema.fields, key=lambda field: field.name)
        }

    def __repr__(self):
        return self._df._jdf.schema().treeString()

    def _repr_html_(self):
        template = Template(self._template_schm)
        return template.render(fields=self._order_action[self._order]())

    _template_schm = """<table>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Nullable</th>
        </tr>
        {% for field in fields %}
        <tr>
            <td align="right"> {{ field.name }} </td>
            <td align="right"> {{ field.dataType.simpleString() }} </td>
            <td align="right">
            {% if field.nullable %}
                &#10003;
            {% else %}

            {% endif %}
            </td>
        </tr>
        {% endfor %}
    </table>
    """

def printSchema(self, order='schm'):
    assert (order in ['schm', 'type', 'alph'])
    return DataFrameSchema(self, order)

DataFrame.printSchema = printSchema
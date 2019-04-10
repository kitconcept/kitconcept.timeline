const makeConfig = require('sc-recipe-staticresources');


module.exports = makeConfig(
  // name
  'kitconcept.timeline',

  // shortName
  'timeline',

  // path
  `${__dirname}/../src/kitconcept/timeline/browser/static`,

  //publicPath
  '++resource++kitconcepttimeline/',
);

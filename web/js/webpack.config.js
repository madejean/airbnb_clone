var congif = {
    entry: './js/app.js',

    output: {
	     path: __dirname,
	     filename: './static/bundle.js',
    }

    module: {
	     loaders: [
	        {
		          exclude: /node_modules/,
		          loader: 'babel-loader',

		            query: {
		                presets: ['es2015', 'react']
		                }
	        }
	      ]
    }
};

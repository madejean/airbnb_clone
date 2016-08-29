var Comment = React.createClass({ //comment component takes data from parent component
    rawMarkup: function() {
        var md = new Remarkable(); //remarkable library call
        var rawMarkup = md.render(this.props.children.toString());
        return { __html: rawMarkup };
    },
    render: function() {
      return (
        <div className="comment">
          <h2 className="commentAuthor">
            {this.props.author} //this.props to access proprety from parent to children
          </h2>
          //converts children to raw string
          <span dangerouslySetInnerHTML={this.rawMarkup()} />
          </div>
    );
  }
});

var CommentBox = React.createClass({ //creates new react component
loadCommentsFromServer: function() {
  $.ajax({
    url: this.props.url,
    dataType: 'json',
    cache: false,
    sucess: function(data) {
      this.setState({data: data}); //dynamically updates the key data
    }.bind(this),
    error: function(xhr, status, err) {
      console.error(this.props.url, status, err.toString());
    }.bind(this)
    });
  },
  //submit to the server to refresh list of comment
  handleCommentSubmit: function(comment) {
    var comments = this.state.data;
    comment.id = Date.now();
    var newComments = comments.concat([comment]);
    this.setState({data: newComments});
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      type: 'POST',
      data: comment,
      sucess: function(data) {
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        this.setState({data: comments});
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
//getInitialState() sets up initial state
  getInitialState: function() {
    return {data:[]};
  },

//React call after is rendered for first time
  componentDidMount: function() {
    this.loadCommentsFromServer();
    setInterval(this.loadCommentsFromServer, this.props.pollInterval);
  },

  render: function() { //render returns a tree of React components to render to HTML
    return (
      <div clasName="commentBox">
      <h1>Comments</h1>
      <CommentList data={this.state.data} />
      <CommentForm onCommentSubmit={this.handleCommentSubmit} />
      </div>
        );
      }
    });

  var CommentList = React.createClass({
    render: function() {
      var commentNodes = this.props.data.map(function(comment) {
        return (
          <Comment author={comment.author} key={comment.id}>
            {comment.text}
          </Comment>
        );
      });
      return (
        <div className="commentList">
          {commentNodes}
        </div>
      );
    }
  });

//creates the commentForm asking for name and text and sending a Request to server to save comment
  var CommentForm= React.createClass({
    getInitialState: function () {
      return {author:'', text:''};
    },
    handleAuthorChange: function(e) {
      this.setState({author: e.target.value});
    },
    handleTextChange: function(e) {
      this.setState({text: e.target.value});
    },
    //prevent the browser's default action of submitting
    handleSubmit: function(e) {
      e.preventDefault();
      var author = this.state.author.trim();
      var text = this.state.text.trim();
      if(!text || !author){
        return;
      }
      //send request to server
      this.props.onCommentSubmit({author: author, text: text});
      this.setState({author:'', text:''});
    },
    render: function() {
      //onSubmit clears fields after submitting
      return (
      <form className="commentForm" onSubmit={this.handleSubmit}>
        <input type="text" placeholder="name"
        value={this.state.author}
        onChange={this.handleAuthorChange} />
        <input type="text" placeholder="add your comment"
        value={this.state.text}
        onChange={this.handleTextChange} />
        <input type="submit" value="Post" />
      </form>
      );
    }
  });

//start framework root component injects markup as DOM element second argument
ReactDOM.render(
  <CommentBox url="/api/comments" pollInterval={2000} />,
  document.getElementById('content')
);

什么是 HTML？
    HTML 是用来描述网页的一种语言。
    HTML 指的是超文本标记语言 (Hyper Text Markup Language)
    HTML 不是一种编程语言，而是一种标记语言 (markup language)
    标记语言是一套标记标签 (markup tag)
    HTML 使用标记标签来描述网页

HTML 标签
    HTML 标记标签通常被称为 HTML 标签 (HTML tag)。
    HTML 标签是由尖括号包围的关键词，比如 <html>
    HTML 标签通常是成对出现的，比如 <b> 和 </b>
    标签对中的第一个标签是开始标签，第二个标签是结束标签
    开始和结束标签也被称为开放标签和闭合标签


HTML 标题（Heading）是通过 <h1> - <h6> 等标签进行定义的。
    #标题的大小依次递减

HTML 段落是通过 <p> 标签进行定义的。
    #段落能自动进行换行

HTML 链接
HTML 链接是通过 <a> 标签进行定义的。
    示例#<a href="http://www.w3school.com.cn">This is a link</a>

HTML 图像
HTML 图像是通过 <img> 标签进行定义的，图像的尺寸可以以属性的方式进行控制。
    <img src="w3school.jpg" width="104" height="142" />

HTML 元素
    HTML 元素指的是从开始标签（start tag）到结束标签（end tag）的所有代码。

HTML 元素语法
    HTML 元素以开始标签起始
    HTML 元素以结束标签终止
    元素的内容是开始标签与结束标签之间的内容
    某些 HTML 元素具有空内容（empty content）
    空元素在开始标签中进行关闭（以开始标签的结束而结束）
    大多数 HTML 元素可拥有属性

嵌套的 HTML 元素
    大多数 HTML 元素可以嵌套（可以包含其他 HTML 元素）。
    HTML 文档由嵌套的 HTML 元素构成。
    以下几个元素的介绍：
         <p> 元素定义了 HTML 文档中的一个段落。
         <body> 元素定义了 HTML 文档的主体。
         <html> 元素定义了整个 HTML 文档。

HTML 属性
    HTML 标签可以拥有属性。属性提供了有关 HTML 元素的更多的信息。
    属性总是以名称/值对的形式出现，比如：name="value"。
    属性总是在 HTML 元素的开始标签中规定。
    属性的格式如下示例：
         <a href="http://www.w3school.com.cn">This is a link</a>  #href为属性，引号里面为值
         <h1 align="center">   #属性的定义在开始标签里面

注释：默认情况下，HTML 会自动地在块级元素前后添加一个额外的空行，比如段落、标题元素前后。

HTML 水平线
    <hr /> 标签在 HTML 页面中创建水平线。
    hr 元素可用于分隔内容。
    <p>This is a paragraph</p>
    <hr />

HTML 注释
    <!-- This is a comment -->

HTML 折行
如果您希望在不产生一个新段落的情况下进行换行（新行），请使用 <br /> 标签：
    <p>This is<br />a para<br />graph with line breaks</p>   #进行了两个换行操作

HTML 的 style 属性
    style 属性的作用：
    提供了一种改变所有 HTML 元素的样式的通用方法。
    样式是 HTML 4 引入的，它是一种新的首选的改变 HTML 元素样式的方式。通过 HTML 样式，能够通过
    使用 style 属性直接将样式添加到 HTML 元素，或者间接地在独立的样式表中（CSS 文件）进行定义。
    示例：
        <html>
            <body style="background-color:yellow">
                <h2 style="background-color:red">This is a heading</h2>
                <p style="background-color:green">This is a paragraph.</p>
            </body>
        </html>

HTML 可定义很多供格式化输出的元素，比如粗体和斜体字。
    理解：提供一套以标签的形式(非标签属性)格式化文本的方法。（提供一些固定的样式）

HTML 引用
    HTML <q> 用于短的引用
    HTML <q> 元素定义短的引用。
    浏览器通常会为 <q> 元素包围引号。
    用于长引用的 HTML <blockquote>
    HTML <blockquote> 元素定义被引用的节。
    浏览器通常会对 <blockquote> 元素进行缩进处理。

用于联系信息的 HTML <address>
    HTML <address> 元素定义文档或文章的联系信息（作者/拥有者）。
    此元素通常以斜体显示。大多数浏览器会在此元素前后添加折行。

HTML 代码格式
    HTML <code> 元素定义编程代码示例：
    由于<code> 元素不保留多余的空格和折行，如果想保留原有的编辑格式的话使用<pre>标签

HTML CSS
    通过使用 HTML4.0，所有的格式化代码均可移出 HTML 文档，然后移入一个独立的样式表。
    使用添加到 <head> 部分的样式信息对 HTML 进行格式化。
    示例：
        <html>
            <head>
                <style type="text/css">
                h1 {color: red}
                p {color: blue}
                </style>
            </head>

            <body>
                <h1>header 1</h1>
                <p>A paragraph.</p>
            </body>
        </html>
     <link> 标签链接到一个外部样式表。

HTML样式的三种使用方式
    外部样式表
    示例：
        <head>
        <link rel="stylesheet" type="text/css" href="mystyle.css">
        </head>
    内部样式表
    head 部分通过 <style> 标签定义内部样式表。
    示例：
        <head>
        <style type="text/css">
        body {background-color: red}
        p {margin-left: 20px}
        </style>
        </head>
    内联样式
    当特殊的样式需要应用到个别元素时，就可以使用内联样式。
        <p style="color: red; margin-left: 20px">
        This is a paragraph
        </p>

HTML 链接
    HTML 使用超级链接与网络上的另一个文档相连。
    几乎可以在所有的网页中找到链接。点击链接可以从一张页面跳转到另一张页面。
    实例:
        <a href="/index.html">本文本</a> 是一个指向本网站中的一个页面的链接。</p>   #创建一个简单的超链接
        <a href="/example/html/lastpage.html">
        <img border="0" src="/i/eg_buttonnext.gif"/>
        </a>   #指定图片作为一个超链接对象
    注意：超链接可以是一个字，一个词，或者一组词，也可以是一幅图像，您可以点击这些内容来跳转到新的文档或者当前文档中的某个部分。
    HTML 链接 - target 属性
        使用 Target 属性，你可以定义被链接的文档在何处显示，譬如在新的窗口页。
        <a href="http://www.w3school.com.cn/" target="_blank">Visit W3School!</a>

    HTML 链接 - name 属性
        name 属性规定锚（anchor）的名称，您可以使用 name 属性创建 HTML 页面中的书签。
        实例：（可用于实现页面内不同部分的跳转）
            <a name="tips">基本的注意事项 - 有用的提示</a>      #name属性可以用id来替换
            <a href="#tips">有用的提示</a>
    链接到同一个页面的不同位置
        使用属性target="_blank"
    跳出框架
        target="_top"   #该属性的请求链接地址页面会（跳出当前页面框架）覆盖当前页面。
    创建电子邮件链接
        <p>
            <a href="mailto:someone@microsoft.com?subject=Hello%20again">发送邮件</a>   #%20为空格，subject为邮件主题
        </p>
图像标签（<img>）和源属性（Src）
    <img> 是空标签，意思是说，它只包含属性，并且没有闭合标签。
    <img src="url" />
替换文本属性（Alt）
    alt 属性用来为图像定义一串预备的可替换的文本。替换文本属性的值是用户定义的。
    <img src="boat.gif" alt="Big Boat">
定义背景使用background
    <body background="/i/eg_background.jpg">
使用 HTML 创建表格
    表格由 <table> 标签来定义。每个表格均有若干行（由 <tr> 标签定义），每行被分割为若干单元格（由 <td> 标签定义）。字母 td
    指表格数据（table data），即数据单元格的内容。数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。
    <table border="1">         #定义表格的标签，border表示是否带边框
    <tr>                       #定义表格的行
    <td>row 1, cell 1</td>     #定义表格里的数据
    <td>row 1, cell 2</td>
    </tr>
    </table>
    表格的表头：表格的表头使用 <th> 标签进行定义。
    <tr>
    <th>Heading</th>
    <th>Another Heading</th>
    </tr>
    <td></td>                       #可以表示为空的占位符
    <th rowspan="2">电话</th>        #表示跨多行的列
HTML 支持有序、无序和定义列表
    <ul>
         <li>咖啡</li>
         <li>茶</li>
         <li>牛奶</li>
    </ul>
    #无序列表
    <ol start="50">
          <li>咖啡</li>
          <li>牛奶</li>
          <li>茶</li>
    </ol>
    #有序列表
    有序与无序列表都可以定义各种各样的属性，可嵌套。
HTML <div> 和 <span>
    可以通过 <div> 和 <span> 将 HTML 元素组合起来。
    HTML 块元素
        大多数 HTML 元素被定义为块级元素或内联元素。
        块级元素在浏览器显示时，通常会以新行来开始（和结束）。
    HTML 内联元素
        内联元素在显示时通常不会以新行开始。
    HTML <div> 元素
        定义：块级元素，用于组合其他HTML元素的容器。
        特性：与 CSS 一同使用，<div> 元素可用于对大的内容块设置样式属性。
        用途：文档布局，取代table的布局方法。
            <div style="color:#00FF00">
              <h3>This is a header</h3>
              <p>This is a paragraph.</p>
            </div>
    HTML <span> 元素
        HTML <span> 元素是内联元素，可用作文本的容器。
        与 CSS 一同使用时，<span> 元素可用于为部分文本设置样式属性。
HTML 类
    对 HTML 进行分类（设置类），使我们能够为元素的类定义 CSS 样式。
    为相同的类设置相同的样式，或者为不同的类设置不同的样式。
    分类块级元素
        <head>
        <style>
        .cities {
            background-color:black;
            color:white;
            margin:20px;
            padding:20px;
        }
        </style>
        </head>
        <div class="cities">
        <h2>London</h2>
        <p>
        London is the capital city of England.
        </p>
        </div>
    分类行内元素
        <h1>My <span class="red">Important</span> Heading</h1>
HTML 布局
    使用 <div> 元素的 HTML 布局
    注释：<div> 元素常用作布局工具，因为能够轻松地通过 CSS 对其进行定位。
    <div id="header">
    <h1>City Gallery</h1>
    </div>

    <div id="nav">
    London<br>
    Paris<br>
    Tokyo<br>
    </div>
    <style>
    #header {
        background-color:black;
        color:white;
        text-align:center;
        padding:5px;
    }
    #nav {
        line-height:30px;
        background-color:#eeeeee;
        height:300px;
        width:100px;
        float:left;
        padding:5px;
    }
    </style>
    使用 HTML5 的网站布局
    HTML5 提供的新语义元素定义了网页的不同部分：

    header	定义文档或节的页眉
    nav	定义导航链接的容器
    section	定义文档中的节
    article	定义独立的自包含文章
    aside	定义内容之外的内容（比如侧栏）
    footer	定义文档或节的页脚
    details	定义额外的细节
    summary	定义 details 元素的标题
HTML 响应式 Web 设计
    什么是响应式 Web 设计？
        RWD 指的是响应式 Web 设计（Responsive Web Design）
        RWD 能够以可变尺寸传递网页
        RWD 对于平板和移动设备是必需的
    使用Bootstrap
        Bootstrap 是最流行的开发响应式 web 的 HTML, CSS, 和 JS 框架。
        Bootstrap 帮助您开发在任何尺寸都外观出众的站点：显示器、笔记本电脑、平板电脑或手机：
HTML 框架
    通过使用框架，你可以在同一个浏览器窗口中显示不止一个页面。
    通过使用框架，你可以在同一个浏览器窗口中显示不止一个页面。每份HTML文档称为一个框架，并且每个框架都独立于其他的框架。
    框架结构标签（<frameset>）
        框架结构标签（<frameset>）定义如何将窗口分割为框架
        每个 frameset 定义了一系列行或列
        rows/columns 的值规定了每行或每列占据屏幕的面积
    实例：
        如何使用 <noframes> 标签
        混合框架结构
        含有 noresize="noresize" 属性的框架结构
        导航框架
        内联框架
        跳转至框架内的一个指定的节
        使用框架导航跳转至指定的节
HTML Iframe
    iframe 用于在网页内显示网页。
    用法：
        <iframe src="demo_iframe.htm" width="200" height="200"></iframe>    #设置内连框架的宽高
        <iframe src="demo_iframe.htm" frameborder="0"></iframe>             #Iframe - 删除边框
        使用 iframe 作为链接的目标
        <iframe src="demo_iframe.htm" name="iframe_a"></iframe>
        <p><a href="http://www.w3school.com.cn" target="iframe_a">W3School.com.cn</a></p>
HTML 脚本
    JavaScript 使 HTML 页面具有更强的动态和交互性。
    介绍：
        HTML script 元素
        <script> 标签用于定义客户端脚本，比如 JavaScript。
        script 元素既可包含脚本语句，也可通过 src 属性指向外部脚本文件。
        必需的 type 属性规定脚本的 MIME 类型。
        JavaScript 最常用于图片操作、表单验证以及内容动态更新。
    示例：
        <script type="text/javascript">
        document.write("<h1>Hello World!</h1>")
        </script>
        <noscript>Your browser does not support JavaScript!</noscript>  #脚本被禁用的时候会显示这些内容
HTML 头部元素
    <title> 标题定义文档的标题，会显示在页面的标签页上。
        定义浏览器工具栏中的标题
        提供页面被添加到收藏夹时显示的标题
        显示在搜索引擎结果中的页面标题

    使用 base 标签使页面中的所有标签在新窗口中打开。  #即使不在超链接中定义_blank属性
    使用 <meta> 元素来描述文档，可用于定义文档的一些属性信息，字符集，文档类型等。
        <meta> 元素来定义文档的关键词。             #搜索引擎会检索匹配这些信息
        http-equiv="Refresh"                     #页面重定向
    HTML <link> 元素
        <link> 标签定义文档与外部资源之间的关系。
        <link> 标签最常用于连接样式表：
        <head>
        <link rel="stylesheet" type="text/css" href="mystyle.css" />
        </head>
    HTML <style> 元素
        <style> 标签用于为 HTML 文档定义样式信息。
        <head>
        <style type="text/css">
        body {background-color:yellow}
        p {color:blue}
        </style>
        </head>
HTML 字符实体
     HTML 中的预留字符必须被替换为字符实体。
     如果希望正确地显示预留字符，我们必须在 HTML 源代码中使用字符实体（character entities）。
     对一些保留字符在文本中的正确显示。
HTML 统一资源定位器
    URL 编码
        URL 只能使用 ASCII 字符集来通过因特网进行发送。
        由于 URL 常常会包含 ASCII 集合之外的字符，URL 必须转换为有效的 ASCII 格式。
        URL 编码使用 "%" 其后跟随两位的十六进制数来替换非 ASCII 字符。
        URL 不能包含空格。URL 编码通常使用 + 来替换空格。
    URL 编码示例
        space	    %20
        linefeed    %0a
        c return	%0d
HTML <!DOCTYPE>
    <!DOCTYPE> 声明帮助浏览器正确地显示网页。
    <!DOCTYPE> 声明
    Web 世界中存在许多不同的文档。只有了解文档的类型，浏览器才能正确地显示文档。
    HTML 也有多个不同的版本，只有完全明白页面中使用的确切 HTML 版本，浏览器才能完全正确地显示出 HTML 页面。
    这就是 <!DOCTYPE> 的用处。<!DOCTYPE> 不是 HTML 标签。它为浏览器提供一项信息（声明），即 HTML 是用什么版本编写的。


XHTML 简介
    XHTML 是以 XML 格式编写的 HTML。
    什么是 XHTML？
        XHTML 指的是可扩展超文本标记语言
        XHTML 与 HTML 4.01 几乎是相同的
        XHTML 是更严格更纯净的 HTML 版本
        XHTML 是以 XML 应用的方式定义的 HTML
        XHTML 是 2001 年 1 月发布的 W3C 推荐标准
        XHTML 得到所有主流浏览器的支持

    文档结构
        XHTML DOCTYPE 是强制性的
        <html> 中的 XML namespace 属性是强制性的
        <html>、<head>、<title> 以及 <body> 也是强制性的
    元素语法
        XHTML 元素必须正确嵌套
        XHTML 元素必须始终关闭
        XHTML 元素必须小写
        XHTML 文档必须有一个根元素
    属性语法
        XHTML 属性必须使用小写
        XHTML 属性值必须用引号包围
        XHTML 属性最小化也是禁止的
    如何从 HTML 转换到 XHTML
        向每张页面的第一行添加 XHTML <!DOCTYPE>
        向每张页面的 html 元素添加 xmlns 属性
        把所有元素名改为小写
        关闭所有空元素
        把所有属性名改为小写
        为所有属性值加引号

HTML 表单
    HTML 表单用于搜集不同类型的用户输入，<form> 元素定义 HTML 表单。
    HTML 表单包含表单元素，表单元素指的是不同类型的 input 元素、复选框、单选按钮、提交按钮等等。
    <input> 元素
        text	定义常规文本输入。
            <input type="text" name="firstname">
        radio	定义单选按钮输入（选择多个选择之一）
            <form>
            <input type="radio" name="sex" value="male" checked>Male
            <br>
            <input type="radio" name="sex" value="female">Female
            </form>
        submit	定义提交按钮（提交表单）
           <input type="submit" value="Submit">
        Action 属性
            通常，表单会被提交到 web 服务器上的网页，但也可以被指定某个服务器脚本来处理
            <form action="action_page.php">
        Method 属性
            method 属性规定在提交表单时所用的 HTTP 方法（GET 或 POST）：
            <form action="action_page.php" method="GET">  #method可以为GET或POST
        Name 属性
            如果要正确地被提交，每个输入字段必须设置一个 name 属性。
    <select> 元素（下拉列表）
        实例：
            <select name="cars">
            <option value="volvo">Volvo</option>
            <option value="saab">Saab</option>
            <option value="fiat">Fiat</option>
            <option value="audi">Audi</option>
            </select>
    <option> 元素定义待选择的选项，预定义的作用。
        实例：<option value="fiat" selected>Fiat</option>
    <textarea> 元素，定义多行输入字段（文本域）。
        <textarea name="message" rows="10" cols="30">
        The cat was playing in the garden.
        </textarea>
    <button> 元素，定义可点击的按钮
        <button type="button" onclick="alert('Hello World!')">Click Me!</button>
HTML 输入类型
    <input> 元素的输入类型
        <input type="text"> 定义供文本输入的单行输入字段
            <input type="text" name="firstname">
        输入类型：password
            <input type="password" name="psw">
        <input type="submit"> 定义提交表单数据至表单处理程序的按钮。
            <input type="submit" value="Submit">
        <input type="radio"> 定义单选按钮。
            <input type="radio" name="sex" value="female">Female
        Input Type: checkbox
            <input type="checkbox" name="vehicle" value="Car">I have a car
            <input type="checkbox" name="vehicle" value="Bike">I have a bike
        <input type="button> 定义按钮。
            <input type="button" onclick="alert('Hello World!')" value="Click Me!">
        <input type="number"> 用于应该包含数字值的输入字段。
            <input type="number" name="quantity" min="1" max="5">
        <input type="date"> 用于应该包含日期的输入字段。
            <input type="date" name="bday">
        <input type="color"> 用于应该包含颜色的输入字段。
            <input type="color" name="favcolor">
        <input type="range"> 用于应该包含一定范围内的值的输入字段。
            <input type="range" name="points" min="0" max="10">
        <input type="month"> 允许用户选择月份和年份。
            <input type="month" name="bdaymonth">
        <input type="week"> 允许用户选择周和年。
            <input type="week" name="week_year">
        <input type="time"> 允许用户选择时间（无时区）。
            <input type="time" name="usr_time">
        <input type="datetime"> 允许用户选择日期和时间（有时区）。
            <input type="datetime" name="bdaytime">
        <input type="datetime-local"> 允许用户选择日期和时间（无时区）。
            <input type="datetime-local" name="bdaytime">
        <input type="email"> 用于应该包含电子邮件地址的输入字段。
            <input type="email" name="email">
        <input type="search"> 用于搜索字段（搜索字段的表现类似常规文本字段）。
            <input type="search" name="googlesearch">
        <input type="tel"> 用于应该包含电话号码的输入字段。
            <input type="tel" name="usrtel">
        <input type="url"> 用于应该包含 URL 地址的输入字段。
            <input type="url" name="homepage">
    HTML Input 属性
        value 属性规定输入字段的初始值：
        readonly 属性规定输入字段为只读（不能修改）：
            <input type="text" name="firstname" value="John" readonly>
        disabled 属性
            disabled 属性规定输入字段是禁用的。
        size 属性规定输入字段的尺寸（以字符计）
            <input type="text" name="firstname" value="John" size="40">
        maxlength 属性规定输入字段允许的最大长度
            <input type="text" name="firstname" maxlength="10">
HTML 多媒体
    Web 上的多媒体指的是音效、音乐、视频和动画。
HTML Object 元素
    <object> 的作用是支持 HTML 助手（插件）。
    HTML 助手（插件）
    辅助应用程序（helper application）是可由浏览器启动的程序。辅助应用程序也称为插件。
    辅助程序可用于播放音频和视频（以及其他）。辅助程序是使用 <object> 标签来加载的。
    使用辅助程序播放视频和音频的一个优势是，您能够允许用户来控制部分或全部播放设置。
    大多数辅助应用程序允许对音量设置和播放功能（比如后退、暂停、停止和播放）的手工（或程序的）控制。








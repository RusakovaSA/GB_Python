<?php
$name = "Русакова Славяна";
$profession = "Директор по развитию";
$city = "Москва";
$email = "zd.rusalova@mail.ru";
$phone = "89998688096";
$skills = [
    [
        'name' => 'Управление проектом',
        'percent' => 70,
    ],
    [
        'name' => 'Управление командой',
        'percent' => 50,
    ],
    [
        'name' => 'Аналитика процессов',
        'percent' => 90,
    ],
];
$work_experience = [
  [
      'name_ogranization' => 'ООО "Ромашка"',
      'date_start' => 'Январь 2014',
      'date_end' => 'Февраль 2017',
      'office' => 'Руководитель отдела продаж',
  ],
  [
    'name_ogranization' => 'ООО "Лютики"',
    'date_start' => 'Март 2017',
    'date_end' => 'Май 2020',
    'office' => 'Региональный директор',
  ],
  [
    'name_ogranization' => 'ООО "Цветочки"',
    'date_start' => 'Июнь 2020',
    'date_end' => 'по настоящее время',
    'office' => 'Директор по развитию',
  ],
];
$education = [
  [
    'institution' => '"Средняя школа № 41"',
    'date_start' => 'Сентябрь 1994',
    'date_end' => 'Май 2003',
    'qualification' => 'Школьник',
  ],
  [
    'institution' => '"Колледж имени В.Н. Татищева"',
    'date_start' => 'Сентябрь 2003',
    'date_end' => 'Май 2006',
    'qualification' => 'Технолог-парикмахер',
  ],
  [
    'institution' => '"Geek Brains"',
    'date_start' => 'Март 2023',
    'date_end' => 'по настоящее время',
    'qualification' => 'Программист',
  ],
]
?>
<!DOCTYPE html>
<html>
<head>
  <title>Мое резюме</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Jost:wght@300&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <style>
    html,
    body,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
      font-family: 'Jost', sans-serif;
    }
  </style>
</head>
<body class="w3-light-grey">
  <!-- Page Container -->
  <div class="w3-content w3-margin-top" style="max-width:1400px;">
    <!-- The Grid -->
    <div class="w3-row-padding">
      <!-- Left Column -->
      <div class="w3-third">
        <div class="w3-white w3-text-grey w3-card-4">
          <div class="w3-display-container">
            <img src="https://sun9-8.userapi.com/impf/c846522/v846522074/c314c/-de4ALrnUs8.jpg?size=604x604&quality=96&sign=d3d918b1c6169d672b1db9e138c93246&c_uniq_tag=XkCoqw5Hp65pnilr0B9l8P5cK3_dKiwoZn0yP0HE0B4&type=album"
              style="width:100%" alt="Avatar">
            <div class="w3-display-bottomleft w3-container w3-text-white">
              <h2><?php echo $name?></h2>
            </div>
          </div>
          <div class="w3-container">
            <p><i class="fa fa-briefcase fa-fw w3-margin-right w3-large w3-text-teal"></i><?=$profession ?></p>
            <p><i class="fa fa-home fa-fw w3-margin-right w3-large w3-text-teal"></i><?=$city ?></p>
            <p><i class="fa fa-envelope fa-fw w3-margin-right w3-large w3-text-teal"></i><?=$email ?></p>
            <p><i class="fa fa-phone fa-fw w3-margin-right w3-large w3-text-teal"></i><?=$phone ?></p>
             <hr>
            <p class="w3-large"><b><i class="fa fa-asterisk fa-fw w3-margin-right w3-text-teal"></i>Навыки</b></p>
            <?php for($i = 0; $i < count($skills); $i++): ?>
            	<p><?= $skills[$i]['name'] ?></p>
            	<div class="w3-light-grey w3-round-xlarge w3-small">
              		<div class="w3-container w3-center w3-round-xlarge w3-teal" style="width:<?= $skills[$i]['percent'] ?>%"><?= $skills[$i]['percent'] ?>%</div>
            	</div>
            <?php endfor;?>
            <br>
            <p class="w3-large w3-text-theme"><b><i class="fa fa-globe fa-fw w3-margin-right w3-text-teal"></i>Языки</b>
            </p>
            <p>Английский</p>
            <div class="w3-light-grey w3-round-xlarge">
              <div class="w3-round-xlarge w3-teal" style="height:24px;width:100%"></div>
            </div>
            <br>
          </div>
        </div>
        <br>
        <!-- End Left Column -->
      </div>
      <!-- Right Column -->
      <div class="w3-twothird">
        <div class="w3-container w3-card w3-white w3-margin-bottom">
          <h2 class="w3-text-grey w3-padding-16"><i
              class="fa fa-suitcase fa-fw w3-margin-right w3-xxlarge w3-text-teal"></i>Опыт работы</h2>
          <?php for($i = 0; $i < count($work_experience); $i++): ?>
            <div class="w3-container">
              <h5 class="w3-opacity"><b><?= $work_experience[$i]['name_ogranization']?></b></h5>
              <h6 class="w3-text-teal"><i class="fa fa-calendar fa-fw w3-margin-right"></i><?= $work_experience[$i]['date_start']?> - <?= $work_experience[$i]['date_end']?></h6>
              <p><?= $work_experience[$i]['office']?></p><br>
            </div>
          <?php endfor;?>
        </div>
        <div class="w3-container w3-card w3-white">
          <h2 class="w3-text-grey w3-padding-16"><i
              class="fa fa-certificate fa-fw w3-margin-right w3-xxlarge w3-text-teal"></i>Образование</h2>
          <?php for($i = 0; $i < count($education); $i++): ?>
          <div class="w3-container">
            <h5 class="w3-opacity"><b><?= $education[$i]['institution']?></b></h5>
            <h6 class="w3-text-teal"><i class="fa fa-calendar fa-fw w3-margin-right"></i><?= $education[$i]['date_start']?> - <?= $education[$i]['date_end']?></h6>
            <p><?= $education[$i]['qualification']?></p>
            <hr>
          </div>
          <?php endfor;?>
        </div>
        <!-- End Right Column -->
      </div>
      <!-- End Grid -->
    </div>
    <!-- End Page Container -->
  </div>
  <!-- Footer -->
  <footer class="w3-container w3-teal w3-center w3-margin-top">
    <p>Find me on social media.</p>
    <i class="fa fa-pinterest-p w3-hover-opacity"></i>
    <i class="fa fa-twitter w3-hover-opacity"></i>
    <i class="fa fa-linkedin w3-hover-opacity"></i>
    <!-- End footer -->
  </footer>
</body>
</html>
<template>
  <section class="venu-map no-padding" id="register">
		<div class="container-fluid">
			<div class="row">
				<div class="col-md-6">
					<div class="bottom-contact">
						<h3>Register For Meetup 3</h3>
            <div class="alert alert-success" id="success-box">
              <strong>Awesome!</strong> Please check your email for confirmation email.<br>See you on <strong>11/11/2017</strong>.
            </div>
						<form id="register-form" class="contact-form-bottom">
	    				<div class="error-container"></div>
							<div class="row">
								<div class="col-md-12">
									<div class="form-group">
									<input class="form-control form-control-name" placeholder="Name" name="name" id="name" type="text" required>
									</div>
								</div>
								<div class="col-md-12">
									<div class="form-group">
										<input class="form-control form-control-email" placeholder="Email" name="email" id="email" 
										type="email" required>
									</div>
								</div>
								<div class="col-md-12">
									<div class="form-group">
										<input class="form-control form-control-github" placeholder="Github Username" name="github" id="subject" required>
									</div>
								</div>
                <div class="col-md-12">
									<div class="form-group">
										<input class="form-control form-control-mobile" placeholder="Mobile No" name="mobile" id="subject" required>
									</div>
								</div>
                <div class="col-md-12">
									<div class="form-group">
										<select name="gender" class="form-control form-control-gender" required>
                      <option value="">Select your gender</option>
                      <option value="MALE">Male</option>
                      <option value="FEMALE">Female</option>
                    </select>
									</div>
								</div>
                <div class="col-md-12">
									<div class="form-group">
										<select name="state" class="form-control form-control-location" required>
                      <option value="">Select you location</option>
                      <option value="JOHOR">Johor</option>
                      <option value="KEDAH">Kedah</option>
                      <option value="KELANTAN">Kelantan</option>
                      <option value="MELAKA">Melaka</option>
                      <option value="NEGERISEMBILAN">Negeri Sembilan</option>
                      <option value="PAHANG">Pahang</option>
                      <option value="PERAK">Perak</option>
                      <option value="PERLIS">Perlis</option>
                      <option value="PULAUPINANG">Pulau Pinang</option>
                      <option value="SABAH">Sabah</option>
                      <option value="SARAWAK">Sawarak</option>
                      <option value="SELANGOR">Selangor</option>
                      <option value="TERENGGANU">Terengganu</option>
                      <option value="KUALALUMPUR">WP Kuala Lumpur</option>
                      <option value="LABUAN">WP Labuan</option>
                      <option value="PUTRAJAYA">WP Putrajaya</option>
                    </select>
									</div>
								</div>
                <div class="col-md-12">
									<div class="form-group">
										<select name="track" class="form-control form-control-track" required>
                      <option value="">Select your class</option>
                      <option value="Android Development">Android Development</option>
                      <option value="Augmented Reality">Augmented Reality</option>
                      <option value="Blockchain">Blockchain</option>
                      <option value="Data Science">Data Science</option>
                      <option value="Game Development">Game Development</option>
                      <option value="Machine Learning">Machine Learning</option>
                      <option value="React Native">React Native</option>
                      <option value="Software Architecture">Software Architecture</option>
                      <option value="Web Development">Web Development (Front-end/Back-end)</option>
                    </select>
									</div>
								</div>
							</div>
							<div class="text-right"><br>
                <input type="hidden" name="type" value="meetup" class="form-control-type">
								<button class="btn btn-primary btn-full" id="submit-registration-form">Register</button> 
							</div>
						</form><!-- Contact form end -->
					</div><!-- Contact form div end -->
				</div><!-- Col end -->
				<div class="col-md-6">
					<div id="map" class="map-bottom"></div> <!-- Google Map -->
				</div><!-- Col end -->
			</div><!-- Content row end -->
		</div><!-- Container end -->
	</section><!-- Map end -->
</template>